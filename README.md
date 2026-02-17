# ArcRaidersCountStash

Automatically calculates your **stash total value** in ARC Raiders.

> ⚠️ Works correctly **ONLY on Full HD (1920×1080)** resolution.  
> Windows display scaling must be set to **100%**.

---

## ✨ Features

- Automatically counts total stash value  
- Simple and lightweight  
- Supports single-monitor setup (`left` option)  

---

## ✅ Requirements

- **Python 3.10+** (recommended)  
- Monitor resolution: **1920×1080 (Full HD)**  
- Windows display scaling: **100%**

---

## 📦 Dependencies

The script uses the following imports:

```python
import tkinter as tk
from tkinter import simpledialog
import pyautogui as p
import keyboard
import time
from collections import deque
