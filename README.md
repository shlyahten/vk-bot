# VKBottle Bot - Portainer Stack Configuration

A Python-based VKontakte bot using the [vkbottle](https://github.com/vkbottle/vkbottle) framework, deployed via Docker Compose in Portainer.

## 📋 Prerequisites

- Docker & Docker Compose installed
- Portainer instance running
- VKontakte Bot Token (from [VK Developers](https://vk.com/dev/bots_docs))

## 🚀 Quick Start

### 1. Clone or Create Project Structure

```bash
mkdir vk-bot
cd vk-bot
```

### 2. Create Required Files

#### `stack.yml` (Portainer Stack Configuration)
This file is already provided - it defines the Docker service configuration.

#### `stack.env` (Environment Variables)
Create a `stack.env` file with your bot token:

```env
VK_TOKEN=your_bot_token_here
```

> ⚠️ **Security Note**: Never commit `stack.env` to version control. Add it to `.gitignore`.

#### `requirements.txt` (Python Dependencies)
```txt
vkbottle>=4.0.0
watchfiles>=0.20.0
```

#### `bot.py` (Your Bot Code)
Example minimal bot:

```python
from vkbottle import Bot
from vkbottle.dispatch.rules.base import MessageRule
import os

bot = Bot(token=os.getenv("VK_TOKEN"))

@bot.message_handler()
async def handler(message):
    await message.answer("Hello! I'm a vkbottle bot.")

if __name__ == "__main__":
    bot.run_forever()
```

### 3. Deploy via Portainer

1. Open Portainer web interface
2. Navigate to **Stacks** → **Add stack**
3. Choose **Web Editor** or **Upload** method
4. Copy contents of `stack.yml` into the editor
5. Click **Deploy the stack**

Alternatively, deploy via CLI:

```bash
docker stack deploy -c stack.yml vkbottle_bot
```

## 📁 Project Structure

```
vk-bot/
├── stack.yml          # Docker Compose configuration
├── stack.env          # Environment variables (DO NOT COMMIT)
├── requirements.txt   # Python dependencies
├── bot.py            # Main bot application
└── .gitignore        # Git ignore file
```

Recommended `.gitignore`:
```gitignore
# Environment files
stack.env
.env
*.env

# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
venv/
ENV/
env/

# IDE
.vscode/
.idea/
*.swp
*.swo

# Logs
*.log
```

## 🔧 Configuration Options

### Service Configuration (`stack.yml`)

| Parameter | Description | Default |
|-----------|-------------|---------|
| `image` | Python base image | `python:3.12-slim` |
| `container_name` | Container name | `vkbottle_bot` |
| `restart` | Restart policy | `unless-stopped` |
| `working_dir` | Working directory inside container | `/app` |
| `volumes` | Host volume mount | `/mnt/HDD/vk-bot:/app` |
| `PYTHONUNBUFFERED` | Disable Python output buffering | `1` |

### Health Check

The container includes a health check that verifies vkbottle is importable:

- **Interval**: 30 seconds
- **Timeout**: 10 seconds
- **Retries**: 3
- **Start Period**: 15 seconds

### Logging

Logs are configured with rotation:

- **Max Size**: 10MB per file
- **Max Files**: 3 files retained

## 🛠 Development

### Local Testing (Without Docker)

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run bot
python bot.py
```

### Hot Reload

The container uses `watchfiles` for automatic reload on Python file changes during development.

### View Logs

**Portainer UI**: Navigate to the container → **Logs** tab

**CLI**:
```bash
docker logs vkbottle_bot -f
```

### Access Container Shell

```bash
docker exec -it vkbottle_bot sh
```

## 🔍 Troubleshooting

### Bot Not Starting

1. Check if `VK_TOKEN` is set correctly in `stack.env`
2. Verify `bot.py` exists in the mounted volume
3. Check container logs: `docker logs vkbottle_bot`

### Import Errors

Ensure `requirements.txt` includes all necessary dependencies:
```txt
vkbottle>=4.0.0
```

### Volume Mount Issues

Verify the host directory exists:
```bash
ls -la /mnt/HDD/vk-bot
```

Ensure proper permissions:
```bash
chmod -R 755 /mnt/HDD/vk-bot
```

### Health Check Failing

The health check verifies vkbottle can be imported. If it fails:
1. Check if `requirements.txt` is present
2. Verify network connectivity for pip install
3. Check container logs for installation errors

## 📦 Updating the Bot

1. Update your `bot.py` or other files in `/mnt/HDD/vk-bot`
2. The container will automatically reload due to `watchfiles`
3. Or restart the stack in Portainer

To update dependencies:
1. Modify `requirements.txt`
2. Restart the stack/container

## 🔐 Security Best Practices

- ✅ Keep `stack.env` out of version control
- ✅ Use strong, unique bot tokens
- ✅ Regularly update base image and dependencies
- ✅ Limit volume mounts to necessary directories only
- ✅ Monitor container logs for suspicious activity

## 📚 Resources

- [vkbottle Documentation](https://vkbottle.readthedocs.io/)
- [vkbottle GitHub Repository](https://github.com/vkbottle/vkbottle)
- [VK Bot API Documentation](https://dev.vk.com/api/bots/getting-started)
- [Docker Compose Reference](https://docs.docker.com/compose/compose-file/)
- [Portainer Documentation](https://docs.portainer.io/)

## 📄 License

This project is open source. The vkbottle framework is licensed under the MIT License.

---

**Made with ❤️ using vkbottle**
