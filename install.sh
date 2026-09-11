#!/usr/bin/env bash

set -e

echo "[*] Starting NexScan setup..."

# -------------------------
# Helper: detect package manager
# -------------------------
install_package() {
    PACKAGE="$1"

    if command -v apt >/dev/null 2>&1; then
        sudo apt update
        sudo apt install -y "$PACKAGE"

    elif command -v pacman >/dev/null 2>&1; then
        sudo pacman -S --needed --noconfirm "$PACKAGE"

    elif command -v dnf >/dev/null 2>&1; then
        sudo dnf install -y "$PACKAGE"

    elif command -v zypper >/dev/null 2>&1; then
        sudo zypper install -y "$PACKAGE"

    else
        echo "[!] Unsupported package manager."
        return 1
    fi
}

# -------------------------
# Check Python 3
# -------------------------
if ! command -v python3 >/dev/null 2>&1; then
    echo "[!] Python 3 not found."
    echo "[*] Installing Python 3..."

    if command -v apt >/dev/null 2>&1; then
        sudo apt update
        sudo apt install -y python3 python3-pip python3-venv

    elif command -v pacman >/dev/null 2>&1; then
        sudo pacman -S --needed --noconfirm python python-pip

    elif command -v dnf >/dev/null 2>&1; then
        sudo dnf install -y python3 python3-pip

    elif command -v zypper >/dev/null 2>&1; then
        sudo zypper install -y python3 python3-pip

    else
        echo "[!] Could not install Python automatically."
        echo "[!] Install Python 3 manually and rerun this script."
        exit 1
    fi
else
    echo "[+] Python 3 found."
fi

# -------------------------
# Check Nmap
# -------------------------
if ! command -v nmap >/dev/null 2>&1; then
    echo "[!] Nmap not found."
    echo "[*] Installing Nmap..."

    if ! install_package "nmap"; then
        echo "[!] Could not install Nmap automatically."
        echo "[!] Install Nmap manually and rerun this script."
        exit 1
    fi
else
    echo "[+] Nmap found."
fi

# -------------------------
# Check virtualenv support
# -------------------------
if ! python3 -m venv --help >/dev/null 2>&1; then
    echo "[!] Python venv support not found."
    echo "[*] Installing venv support..."

    if command -v apt >/dev/null 2>&1; then
        sudo apt update
        sudo apt install -y python3-venv

    elif command -v dnf >/dev/null 2>&1; then
        sudo dnf install -y python3

    elif command -v pacman >/dev/null 2>&1; then
        sudo pacman -S --needed --noconfirm python

    elif command -v zypper >/dev/null 2>&1; then
        sudo zypper install -y python3

    else
        echo "[!] Could not install venv support automatically."
        exit 1
    fi
fi

# -------------------------
# Create virtual environment
# -------------------------
if [ ! -d ".venv" ]; then
    echo "[*] Creating virtual environment..."
    python3 -m venv .venv
else
    echo "[+] Virtual environment found."
fi

# -------------------------
# Upgrade pip
# -------------------------
echo "[*] Upgrading pip..."
.venv/bin/python -m pip install --upgrade pip

# -------------------------
# Install Python dependencies
# -------------------------
if [ -f "requirements.txt" ]; then
    echo "[*] Installing Python dependencies..."
    .venv/bin/python -m pip install -r requirements.txt
else
    echo "[!] requirements.txt not found."
    exit 1
fi

# -------------------------
# Verify Python dependencies
# -------------------------
echo "[*] Verifying Python dependencies..."

.venv/bin/python -c "import rich, lxml" 2>/dev/null || {
    echo "[!] Python dependency verification failed."
    exit 1
}

# -------------------------
# Verify Nmap
# -------------------------
if ! command -v nmap >/dev/null 2>&1; then
    echo "[!] Nmap verification failed."
    exit 1
fi

# -------------------------
# Create NexScan launcher
# -------------------------
echo "[*] Creating NexScan launcher..."

cat > nexscan << 'EOF'
#!/usr/bin/env bash

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

exec "$SCRIPT_DIR/.venv/bin/python" \
    "$SCRIPT_DIR/nexscan.py" "$@"
EOF

chmod +x nexscan

# -------------------------
# Complete
# -------------------------
echo
echo "[+] NexScan setup completed successfully."
echo
echo "Run NexScan with:"
echo
echo "    ./nexscan"
echo
