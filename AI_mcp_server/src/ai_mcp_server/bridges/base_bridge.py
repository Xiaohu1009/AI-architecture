"""
Base bridge class for platform connections
"""

import asyncio
import socket
import json
import logging
from abc import ABC, abstractmethod
from typing import Dict, Any, Optional
from dataclasses import dataclass


@dataclass
class ConnectionConfig:
    """Connection configuration"""
    host: str
    port: int
    timeout: float
    auto_reconnect: bool


class BaseBridge(ABC):
    """Base class for platform bridges"""
    
    def __init__(self, config: ConnectionConfig, logger: logging.Logger):
        self.config = config
        self.logger = logger
        self.socket: Optional[socket.socket] = None
        self.connected = False
        self._lock = asyncio.Lock()
    
    async def initialize(self) -> None:
        """Initialize the bridge"""
        self.logger.info(f"Initializing {self.__class__.__name__}")
        await self.connect()
    
    async def cleanup(self) -> None:
        """Cleanup the bridge"""
        self.logger.info(f"Cleaning up {self.__class__.__name__}")
        await self.disconnect()
    
    async def connect(self) -> bool:
        """Connect to the platform"""
        async with self._lock:
            if self.connected:
                return True
            
            try:
                self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.socket.settimeout(self.config.timeout)
                self.socket.connect((self.config.host, self.config.port))
                self.connected = True
                self.logger.info(f"Connected to {self.config.host}:{self.config.port}")
                return True
            except Exception as e:
                self.logger.error(f"Failed to connect to {self.config.host}:{self.config.port}: {e}")
                self.connected = False
                return False
    
    async def disconnect(self) -> None:
        """Disconnect from the platform"""
        async with self._lock:
            if self.socket:
                try:
                    self.socket.close()
                except Exception as e:
                    self.logger.error(f"Error closing socket: {e}")
                finally:
                    self.socket = None
                    self.connected = False
                    self.logger.info("Disconnected")
    
    async def check_connection(self) -> bool:
        """Check if connection is alive"""
        if not self.connected or not self.socket:
            return False
        
        try:
            # Try to send a ping command
            await self.send_command("ping", {})
            return True
        except Exception:
            self.connected = False
            return False
    
    async def send_command(self, command_type: str, params: Dict[str, Any] = None) -> Dict[str, Any]:
        """Send command to the platform"""
        if params is None:
            params = {}
        
        # Ensure connection
        if not self.connected:
            if not await self.connect():
                raise ConnectionError(f"Failed to connect to {self.config.host}:{self.config.port}")
        
        command = {
            "type": command_type,
            "params": params
        }
        
        try:
            # Send command
            command_json = json.dumps(command)
            self.socket.sendall((command_json + "\n").encode("utf-8"))
            self.logger.debug(f"Sent command: {command_type}")
            
            # Receive response
            response_data = await self._receive_response()
            response = json.loads(response_data.decode("utf-8"))
            
            if response.get("status") == "error":
                raise Exception(response.get("message", "Unknown error"))
            
            return response.get("result", {})
            
        except Exception as e:
            self.logger.error(f"Error sending command {command_type}: {e}")
            if self.config.auto_reconnect:
                self.connected = False
                await self.connect()
            raise
    
    async def _receive_response(self) -> bytes:
        """Receive response from the platform"""
        if not self.socket:
            raise ConnectionError("Socket not connected")
        
        chunks = []
        buffer_size = 8192
        
        try:
            while True:
                chunk = self.socket.recv(buffer_size)
                if not chunk:
                    break
                
                chunks.append(chunk)
                
                # Check if we have complete JSON
                try:
                    data = b''.join(chunks)
                    json.loads(data.decode('utf-8'))
                    return data
                except json.JSONDecodeError:
                    continue
                    
        except socket.timeout:
            raise Exception("Timeout waiting for response")
        except Exception as e:
            raise Exception(f"Error receiving response: {e}")
    
    @abstractmethod
    async def ping(self) -> Dict[str, Any]:
        """Platform-specific ping implementation"""
        pass
