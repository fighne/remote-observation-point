# remote-observation-point
Raspberry Pi B to be low power remote observation platform.
Initially using Python then moving to Common Lisp (SBCL).

1. Initial base is Raspbian lite
2. platform is Raspberry Pi B 256MB
3. Strinity Sensors Cobber v0.1 -
- a)TLS2561 - https://github.com/adafruit/Adafruit_CircuitPython_TSL2561
- b)BMP180 - https://github.com/jposada202020/CircuitPython_BMP180
- c)AM2321 - https://github.com/adafruit/Adafruit_CircuitPython_AM2320
4. BME280 - https://github.com/adafruit/Adafruit_CircuitPython_BME280
5. GY-271 - https://github.com/jposada202020/CircuitPython_qmc5883l/tree/master
6. VL6180X - https://github.com/adafruit/Adafruit_CircuitPython_VL6180X/tree/main
7. PCA9685 (Waveshare Servo Driver Hat)
8. AM2302 - external temperature and humdity
9. Raspberry Pi NOIR Camera

.nb - raspbian comes pre-installed with Python 3

.nb - bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c, address=0x76) <= if using none Adafruit BME280 board
