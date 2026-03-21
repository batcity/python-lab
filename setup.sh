#!/usr/bin/env bash

set -o pipefail

VENV_DIR=".venv"
PYTHON_BIN="${PYTHON_BIN:-python3}"

echo "🔧 Setting up Python environment (sourced mode)..."

# 1. Check python exists
if ! command -v "$PYTHON_BIN" >/dev/null 2>&1; then
    echo "❌ Python not found: $PYTHON_BIN"
    return 1
fi

# 2. Create venv if needed
if [ ! -d "$VENV_DIR" ]; then
    echo "📦 Creating virtual environment..."
    "$PYTHON_BIN" -m venv "$VENV_DIR" || {
        echo "❌ Failed to create venv"
        return 1
    }
else
    echo "✅ Virtual environment already exists"
fi

# 3. Activate (this is WHY we source)
ACTIVATE_SCRIPT="$VENV_DIR/bin/activate"
if [ ! -f "$ACTIVATE_SCRIPT" ]; then
    echo "❌ Activation script missing"
    return 1
fi

echo "⚡ Activating virtual environment..."
# shellcheck disable=SC1090
source "$ACTIVATE_SCRIPT"

# 4. Ensure pip exists
if ! python -m pip --version >/dev/null 2>&1; then
    echo "📦 Installing pip..."
    python -m ensurepip --upgrade || {
        echo "❌ Failed to install pip"
        return 1
    }
fi

# 5. Upgrade pip
echo "⬆️ Upgrading pip..."
python -m pip install --upgrade pip || \
    echo "⚠️ pip upgrade failed, continuing..."

# 6. Install deps
install_if_missing () {
    PACKAGE=$1
    if ! python -m pip show "$PACKAGE" >/dev/null 2>&1; then
        echo "📥 Installing $PACKAGE..."
        python -m pip install "$PACKAGE" || \
            echo "⚠️ Failed to install $PACKAGE"
    else
        echo "✅ $PACKAGE already installed"
    fi
}

if [ -f "requirements.txt" ]; then
    echo "📜 Installing from requirements.txt..."
    python -m pip install -r requirements.txt || \
        echo "⚠️ Some installs failed"
else
    install_if_missing requests
    install_if_missing httpx
fi

echo ""
echo "🎉 Setup complete! (venv is ACTIVE in this shell)"