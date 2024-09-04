from machine import Pin, SPI
import time
from lora import LoRa

received_message = None

def reset_lora(reset_pin):
    reset_pin.value(0)
    time.sleep_ms(100)
    reset_pin.value(1)
    time.sleep_ms(100)

def initialize_lora():  
    CS = Pin(10, Pin.OUT)
    RX = Pin(20, Pin.IN)
    RESET = Pin(8, Pin.OUT)
    spi = SPI(0, baudrate=1000000, polarity=0, phase=0, sck=Pin(6), mosi=Pin(7), miso=Pin(4))
    reset_lora(RESET)
    lora = LoRa(spi, cs=CS, rx=RX)
    return lora

def configure_lora(lora):
    lora.set_frequency(868.0)
    lora.set_bandwidth(250000)
    lora.set_spreading_factor(10)
    lora.set_coding_rate(5)
    lora.set_preamble_length(4)
    lora.set_crc(True)
    lora.set_tx_power(24)

def on_receive(payload):
    global received_message
    received_message = payload.decode()
    print("Received message:", received_message)

def set_receive_callback(lora):
    lora.on_recv(on_receive)

def toggle_receiver_mode(lora):
    lora.recv()
    
def toggle_sender_mode(lora, message):
    lora.send(message)

