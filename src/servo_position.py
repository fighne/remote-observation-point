# attributed to :Claude Code
import board
import busio
from adafruit_pca9685 import PCA9685
from adafruit_motor import servo

# Initialize I2C and PCA9685
i2c = busio.I2C(board.SCL, board.SDA)
pca = PCA9685(i2c)
pca.frequency = 50  # Standard servo frequency (50Hz)

# Create servo objects for all 16 channels
servos = [servo.Servo(pca.channels[i]) for i in range(16)]

def set_servo(channel: int, position: int) -> None:
    """
    Control a servo motor position via PCA9685.

    Args:
        channel  (int): PCA9685 channel number (0–15)
        position (int): Servo angle in degrees (0–180)

    Raises:
        ValueError: If channel or position is out of valid range
    """
    if not 0 <= channel <= 15:
        raise ValueError(f"Channel must be 0–15, got {channel}")
    if not 0 <= position <= 180:
        raise ValueError(f"Position must be 0–180 degrees, got {position}")

    servos[channel].angle = position
    print(f"Channel {channel} → {position}°")


# --- Usage Examples ---
set_servo(0, 90)   # Center servo on channel 0
set_servo(1, 0)    # Move servo on channel 1 to minimum
set_servo(2, 180)  # Move servo on channel 2 to maximum
