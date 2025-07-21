# GhostTalk_v2 - Anonymous P2P Messaging

A Python-based anonymous messaging system that implements onion routing for secure and private communication. Messages are encrypted through multiple relay nodes before reaching the chat server, providing layers of anonymity similar to the Tor network.

![Python](https://img.shields.io/badge/Python-3.7+-blue?style=for-the-badge&logo=python)
![Encryption](https://img.shields.io/badge/Encryption-Fernet-green?style=for-the-badge)
![Anonymous](https://img.shields.io/badge/Anonymous-Onion%20Routing-purple?style=for-the-badge)

## 🚀 Features

### 🔐 Privacy & Security
- **Onion Routing**: Messages pass through multiple encrypted layers
- **Multi-Hop Encryption**: Each relay node adds/removes encryption layer
- **Anonymous Nicknames**: Randomly generated user identities
- **End-to-End Protection**: No single node can trace message origin
- **Random Path Selection**: Dynamic routing through relay network

### 🌐 Network Architecture
- **Decentralized Relays**: Multiple relay nodes for redundancy
- **Random Hop Selection**: Unpredictable message paths
- **Broadcast Chat**: Real-time group messaging
- **Multi-Component System**: Separate relay, chat, and client components

### 💬 User Experience
- **Simple CLI Interface**: Easy-to-use command-line chat
- **Real-time Messaging**: Instant message delivery
- **Anonymous Identity**: No registration or personal info required
- **Multiple Modes**: Run as relay node, chat server, or client

## 📋 Requirements

### Dependencies
```bash
pip install cryptography
```

### System Requirements
- Python 3.7 or higher
- Network access for socket connections
- Multiple terminal windows for full network simulation

## 🛠️ Installation & Setup

### 1. Clone or Download
```bash
# Download the onion_chat.py file
wget https://example.com/onion_chat.py
# or create the file with the provided code
```

### 2. Install Dependencies
```bash
pip install cryptography
```

### 3. Network Configuration
The system uses these default ports:
- **Relay Nodes**: 5001, 5002, 5003
- **Chat Server**: 6000
- **Host**: 127.0.0.1 (localhost)

## 🚀 Usage Guide

### Running the Complete Network

**Step 1: Start Relay Nodes**
```bash
# Terminal 1
python onion_chat.py
> Mode? (node/chat/server): node
> Enter port [5001, 5002, 5003]: 5001

# Terminal 2  
python onion_chat.py
> Mode? (node/chat/server): node
> Enter port [5001, 5002, 5003]: 5002

# Terminal 3
python onion_chat.py
> Mode? (node/chat/server): node
> Enter port [5001, 5002, 5003]: 5003
```

**Step 2: Start Chat Server**
```bash
# Terminal 4
python onion_chat.py
> Mode? (node/chat/server): server
```

**Step 3: Connect Clients**
```bash
# Terminal 5 (User 1)
python onion_chat.py
> Mode? (node/chat/server): chat
[You are alice]
Type your messages:
> Hello, anonymous world!

# Terminal 6 (User 2)
python onion_chat.py
> Mode? (node/chat/server): chat
[You are bob42]
Type your messages:
> Hi there! This is so secure!
```

### Example Session
```
[You are ghost]
Type your messages:
> This message will be encrypted through 3 random nodes

alice: Hello everyone! 
bob42: Anyone else loving this anonymous chat?

> My identity is completely hidden!
charlie: The onion routing is working perfectly
```

## 🏗️ Architecture Deep Dive

### System Components

```
┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│    Client   │    │ Relay Node  │    │ Chat Server │
│   (Users)   │◄──►│  Network    │◄──►│  (Hub)      │
└─────────────┘    └─────────────┘    └─────────────┘
```

### Message Flow

```
[Client] → [Encrypt Layer 3] → [Node 5001] → [Decrypt Layer 3]
           ↓
[Encrypt Layer 2] → [Node 5002] → [Decrypt Layer 2]  
           ↓
[Encrypt Layer 1] → [Node 5003] → [Decrypt Layer 1]
           ↓
[Plain Message] → [Chat Server] → [Broadcast to All]
```

### Encryption Process

1. **Client Side**: 
   - Selects 3 random relay nodes
   - Encrypts message with Node3's key
   - Encrypts result with Node2's key  
   - Encrypts result with Node1's key

2. **Relay Nodes**:
   - Each node decrypts one layer
   - Forwards to next hop or final destination
   - No node sees both origin and destination

3. **Chat Server**:
   - Receives plaintext message
   - Broadcasts to all connected clients
   - No knowledge of original sender

## 🔧 Technical Specifications

### Encryption Details
- **Algorithm**: Fernet (AES 128-bit in CBC mode)
- **Key Generation**: Cryptographically secure random keys
- **Layer Encryption**: Multiple encryption layers (onion-style)
- **Forward Secrecy**: Keys generated per session

### Network Protocol
- **Transport**: TCP sockets
- **Port Range**: 5001-6000
- **Connection**: Point-to-point between nodes
- **Reliability**: TCP ensures message delivery

### Routing Algorithm
- **Path Selection**: Random 3-hop paths
- **Hop Probability**: 70% chance to forward to another node
- **Destination**: 30% chance to send to chat server
- **Load Balancing**: Distributed across available nodes

## ⚙️ Configuration Options

### Customizing Network Topology
```python
# Modify these variables in the code:
HOST = '127.0.0.1'              # Change for remote nodes
NODE_PORTS = [5001, 5002, 5003] # Add more relay nodes
CHAT_PORT = 6000                # Chat server port

# Routing probabilities
if random.random() > 0.3:       # Adjust forwarding probability
```

### Adding More Relay Nodes
```python
NODE_PORTS = [5001, 5002, 5003, 5004, 5005]  # Expand network
```

### Security Hardening
```python
# Increase path length for more anonymity
path = random.sample(NODE_PORTS, k=5)  # 5 hops instead of 3
```

## 🚧 Development Roadmap

### Current Features ✅
- [x] Multi-layer onion encryption
- [x] Random relay node routing  
- [x] Real-time chat broadcasting
- [x] Anonymous nickname generation
- [x] CLI interface

### Planned Enhancements 📋
- [ ] GUI client interface
- [ ] File transfer support
- [ ] Better error handling and reconnection
- [ ] Network discovery protocol
- [ ] Message persistence options
- [ ] User authentication (optional)

### Advanced Features 🎯
- [ ] Directory service for node discovery
- [ ] Bandwidth monitoring and optimization
- [ ] Geographic distribution of nodes
- [ ] Mobile client applications
- [ ] Web-based interface

## 🛡️ Security Considerations

### Current Security Model
- **Traffic Analysis**: Multiple hops prevent traffic correlation
- **Message Privacy**: Multi-layer encryption protects content
- **Identity Protection**: Random nicknames maintain anonymity
- **Network Resilience**: Multiple relay nodes provide redundancy

### Known Limitations
- **Local Network Only**: Currently runs on localhost
- **No Perfect Forward Secrecy**: Keys persist during session
- **Timing Attacks**: Message timing could reveal patterns
- **Exit Node Visibility**: Chat server sees final messages
- **No Authentication**: Anyone can join the network

### Security Best Practices
1. **Run Real Distributed Network**: Deploy nodes on different machines
2. **Use VPN/Proxy**: Additional layer of IP protection
3. **Regular Key Rotation**: Restart nodes to generate new keys
4. **Traffic Padding**: Add dummy messages to obscure patterns
5. **Secure Hosting**: Use secure, anonymous hosting for nodes

## 🐛 Troubleshooting

### Common Issues

**Port Already in Use**
```bash
# Error: [Errno 48] Address already in use
# Solution: Kill processes using the ports
lsof -ti:5001 | xargs kill -9
```

**Connection Refused**
```bash
# Error: [Errno 61] Connection refused
# Solution: Ensure relay nodes are running before starting clients
```

**Import Errors**
```bash
# Error: ModuleNotFoundError: No module named 'cryptography'
# Solution: Install dependencies
pip install cryptography
```

**No Messages Received**
```bash
# Issue: Client not receiving messages
# Solution: Check that chat server is running and accessible
```

### Debugging Tips

1. **Check Process Status**:
   ```bash
   netstat -an | grep LISTEN | grep -E '500[1-3]|6000'
   ```

2. **Monitor Network Activity**:
   ```bash
   tcpdump -i lo port 5001 or port 5002 or port 5003 or port 6000
   ```

3. **Add Debug Logging**:
   ```python
   print(f"[DEBUG] Sending via path: {path}")
   print(f"[DEBUG] Message encrypted: {len(payload)} bytes")
   ```

## 🤝 Contributing

### How to Contribute
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Test your changes thoroughly
4. Commit your changes (`git commit -m 'Add amazing feature'`)
5. Push to the branch (`git push origin feature/amazing-feature`)
6. Open a Pull Request

### Development Guidelines
- **Security First**: All changes must maintain or improve security
- **Python Standards**: Follow PEP 8 style guidelines
- **Error Handling**: Add proper exception handling
- **Documentation**: Update README for user-facing changes
- **Testing**: Test with multiple nodes and clients

### Code Style
```python
# Use descriptive variable names
relay_nodes = [5001, 5002, 5003]  # Good
ports = [5001, 5002, 5003]        # Acceptable  
p = [5001, 5002, 5003]            # Avoid

# Add comments for complex logic
for port in reversed(path):  # Build onion layers inside-out
    payload = ciphers[port].encrypt(payload)
```

## 📄 License

This project is released under the MIT License. See LICENSE file for details.

### Third-Party Dependencies
- **cryptography**: BSD/Apache License
- **Python Standard Library**: Python Software Foundation License

## ⚠️ Legal Disclaimer

- This software is for educational and legitimate privacy purposes
- Users are responsible for compliance with local laws
- Not intended for illegal activities
- Respect others' privacy and rights

## 🙏 Acknowledgments

- **Tor Project**: Inspiration for onion routing design
- **Cryptography Library**: Robust encryption implementation
- **Python Community**: Excellent networking and crypto libraries
- **Privacy Researchers**: Foundational work on anonymous communication

## 📞 Support

### Getting Help
- **Issues**: Report bugs and request features via GitHub issues
- **Documentation**: Check this README and inline code comments
- **Community**: Join privacy-focused development communities

### Security Reporting
- **Private Issues**: Email security issues privately
- **Responsible Disclosure**: Allow time for fixes before public disclosure
- **Anonymity**: Use anonymous communication channels when possible

---



![Made with Privacy](https://img.shields.io/badge/Made%20with-Privacy%20in%20Mind-success?style=flat-square)
![Educational](https://img.shields.io/badge/Purpose-Educational-blue?style=flat-square)
![Python](https://img.shields.io/badge/Language-Python-yellow?style=flat-square)
