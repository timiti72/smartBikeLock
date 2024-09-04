from machine import I2C, Pin
from struct import unpack as unp
from math import atan2, degrees, pi

class MPU6050:
    mpu_addr = 0x68  # address of MPU6050
    _I2Cerror = "I2C communication failure"
    
    def __init__(self, i2c, disable_interrupts=False):
        self.i2c = i2c
        self._timeout = 10
        self.disable_interrupts = disable_interrupts

        # Check if MPU6050 is connected
        self.chip_id = int(unp('>h', self._read(1, 0x75, self.mpu_addr))[0])

        # Wake it up
        self.wake()
        self.accel_range(1)
        self._ar = self.accel_range()
        self.gyro_range(0)
        self._gr = self.gyro_range()

    def _read(self, count, memaddr, devaddr):
        return self.i2c.readfrom_mem(devaddr, memaddr, count)

    def _write(self, data, memaddr, devaddr):
        self.i2c.writeto_mem(devaddr, memaddr, bytes([data]))

    def wake(self):
        try:
            self._write(0x01, 0x6B, self.mpu_addr)
        except OSError:
            print(MPU6050._I2Cerror)
        return 'awake'

    def sleep(self):
        try:
            self._write(0x40, 0x6B, self.mpu_addr)
        except OSError:
            print(MPU6050._I2Cerror)
        return 'asleep'

    def sample_rate(self, rate=None):
        gyro_rate = 8000  # Hz
        try:
            if rate is not None:
                rate_div = int(gyro_rate / rate - 1)
                if rate_div > 255:
                    rate_div = 255
                self._write(rate_div, 0x19, self.mpu_addr)
            rate = gyro_rate / (unp('<H', self._read(1, 0x19, self.mpu_addr))[0] + 1)
        except OSError:
            rate = None
        return rate

    def accel_range(self, accel_range=None):
        try:
            if accel_range is not None:
                ar = (0x00, 0x08, 0x10, 0x18)
                self._write(ar[accel_range], 0x1C, self.mpu_addr)
            ari = int(unp('<H', self._read(1, 0x1C, self.mpu_addr))[0] / 8)
        except OSError:
            ari = None
        if ari is not None:
            self._ar = ari
        return ari

    def gyro_range(self, gyro_range=None):
        try:
            if gyro_range is not None:
                gr = (0x00, 0x08, 0x10, 0x18)
                self._write(gr[gyro_range], 0x1B, self.mpu_addr)
            gri = int(unp('<H', self._read(1, 0x1B, self.mpu_addr))[0] / 8)
        except OSError:
            gri = None
        if gri is not None:
            self._gr = gri
        return gri

    def get_accel_raw(self):
        try:
            axyz = self._read(6, 0x3B, self.mpu_addr)
        except OSError:
            axyz = b'\x00\x00\x00\x00\x00\x00'
        return axyz

    def get_acc(self, xyz=None):
        if xyz is None:
            xyz = 'xyz'
        scale = (16384, 8192, 4096, 2048)
        raw = self.get_accel_raw()
        axyz = {'x': unp('>h', raw[0:2])[0] / scale[self._ar],
                'y': unp('>h', raw[2:4])[0] / scale[self._ar],
                'z': unp('>h', raw[4:6])[0] / scale[self._ar]}
        return [axyz[char] for char in xyz]

    def get_gyro_raw(self):
        try:
            gxyz = self._read(6, 0x43, self.mpu_addr)
        except OSError:
            gxyz = b'\x00\x00\x00\x00\x00\x00'
        return gxyz

    def get_gyro(self, xyz=None, use_radians=False):
        if xyz is None:
            xyz = 'xyz'
        scale = (7150, 3755, 1877.5, 938.75) if use_radians else (131.0, 65.5, 32.8, 16.4)
        raw = self.get_gyro_raw()
        gxyz = {'x': unp('>h', raw[0:2])[0] / scale[self._gr],
                'y': unp('>h', raw[2:4])[0] / scale[self._gr],
                'z': unp('>h', raw[4:6])[0] / scale[self._gr]}
        return [gxyz[char] for char in xyz]

