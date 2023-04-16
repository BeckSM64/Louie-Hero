#!/bin/env python3

import os
import argparse
from n64RomConverter import *

# reads in the rom file and return a byte array
def read_file(fname, output_dir):

    file = os.path.join(output_dir, fname)
    with open(file, "rb") as f:

        file_array = bytearray(f.read())

        # TODO: DEBUG, remove later
        # SB T6, 0xE41B(AT)
        file_array[0x0000262C] = 0xA0
        file_array[0x0000262D] = 0x2E
        file_array[0x0000262E] = 0xE4
        file_array[0x0000262F] = 0x1B

        # NOP the instructions that prevent the game from loading with a bad CRC
        # so I don't have to write my own checksum utility cause I'm lazy
        file_array[0x0000066C] = 0x0
        file_array[0x0000066D] = 0x0
        file_array[0x0000066E] = 0x0
        file_array[0x0000066F] = 0x0
        file_array[0x00000678] = 0x0
        file_array[0x00000679] = 0x0
        file_array[0x0000067A] = 0x0
        file_array[0x0000067B] = 0x0

        # Force every level to use Louie as the bomber type
        # ADDIU T0, R0, $0006
        file_array[0x000745C0] = 0x24
        file_array[0x000745C1] = 0x08
        file_array[0x000745C2] = 0x00
        file_array[0x000745C3] = 0x06

        # Removes interaction between Louie and launcher in Battle Room
        # ADDIU T9, R0, $0001
        file_array[0x00078C40] = 0x24
        file_array[0x00078C41] = 0x19
        file_array[0x00078C42] = 0x00
        file_array[0x00078C43] = 0x01

        # Removes interaction between Louie and vents in Air Room
        # ADDIU T0, R0, $0001
        file_array[0x00078E14] = 0x24
        file_array[0x00078E15] = 0x08
        file_array[0x00078E16] = 0x00
        file_array[0x00078E17] = 0x01

        # Remove the door in hades crater
        file_array[0x00220860] = 0x00
        file_array[0x00220861] = 0x00
        file_array[0x00220862] = 0x00
        file_array[0x00220863] = 0x00
        file_array[0x00220864] = 0x00
        file_array[0x00220865] = 0x00
        file_array[0x00220866] = 0x00
        file_array[0x00220867] = 0x00

        # Remove the door on the cage in death temple
        file_array[0x00221A30] = 0x00
        file_array[0x00221A31] = 0x00
        file_array[0x00221A32] = 0x00
        file_array[0x00221A33] = 0x00
        file_array[0x00221A34] = 0x00
        file_array[0x00221A35] = 0x00
        file_array[0x00221A36] = 0x00
        file_array[0x00221A37] = 0x00

        # Replace final turret with box in Aquaway
        file_array[0x00222780] = 0x00
        file_array[0x00222781] = 0x41

        # Remove mirror room mirror bomber
        file_array[0x002256E0] = 0x00
        file_array[0x002256E1] = 0x00
        file_array[0x002256E2] = 0x00
        file_array[0x002256E3] = 0x00
        file_array[0x002256E4] = 0x00
        file_array[0x002256E5] = 0x00
        file_array[0x002256E6] = 0x00
        file_array[0x002256E7] = 0x00

        # Remove mirror room mirror door
        file_array[0x002256F0] = 0x00
        file_array[0x002256F1] = 0x00
        file_array[0x002256F2] = 0x00
        file_array[0x002256F3] = 0x00
        file_array[0x002256F4] = 0x00
        file_array[0x002256F5] = 0x00
        file_array[0x002256F6] = 0x00
        file_array[0x002256F7] = 0x00

        # Remove mirror room switch
        file_array[0x00225700] = 0x00
        file_array[0x00225701] = 0x00
        file_array[0x00225702] = 0x00
        file_array[0x00225703] = 0x00
        file_array[0x00225704] = 0x00
        file_array[0x00225705] = 0x00
        file_array[0x00225706] = 0x00
        file_array[0x00225707] = 0x00

        # Remove mirror room door
        file_array[0x00225710] = 0x00
        file_array[0x00225711] = 0x00
        file_array[0x00225712] = 0x00
        file_array[0x00225713] = 0x00
        file_array[0x00225714] = 0x00
        file_array[0x00225715] = 0x00
        file_array[0x00225716] = 0x00
        file_array[0x00225717] = 0x00

        # Remove mirror room switch
        file_array[0x00225720] = 0x00
        file_array[0x00225721] = 0x00
        file_array[0x00225722] = 0x00
        file_array[0x00225723] = 0x00
        file_array[0x00225724] = 0x00
        file_array[0x00225725] = 0x00
        file_array[0x00225726] = 0x00
        file_array[0x00225727] = 0x00

        # Remove mirror room door
        file_array[0x00225730] = 0x00
        file_array[0x00225731] = 0x00
        file_array[0x00225732] = 0x00
        file_array[0x00225733] = 0x00
        file_array[0x00225734] = 0x00
        file_array[0x00225735] = 0x00
        file_array[0x00225736] = 0x00
        file_array[0x00225737] = 0x00

        # Change starting position for Rockn' Road
        file_array[0x000F8E24] = 0xFD
        file_array[0x000F8E25] = 0x6C
        file_array[0x000F8E26] = 0xFF
        file_array[0x000F8E27] = 0xE2
        file_array[0x000F8E28] = 0x30
        file_array[0x000F8E29] = 0x0C
        file_array[0x000F8E2A] = 0x00
        file_array[0x000F8E2B] = 0x00

        return file_array

# writes the modified data back to the rom
def write_file(fname, output_dir, data):

    file = os.path.join(output_dir, fname)
    with open(file, "wb") as f:
        f.write(data)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_rom", help="The clean Bomberman Hero ROM", type=str)
    parser.add_argument("output_dir", help="The directory to place the generated ROM. Output ROM will be named <input_rom>.rando.z64", type=str)
    args = parser.parse_args()

    # get file as input
    input_name = args.input_rom

    # get output dir
    output_dir = args.output_dir

    # output file name
    output_file = "louieHero.z64"

    convertRom(input_name, output_file, output_dir)

    # read ROM
    rom_data = read_file(output_file, output_dir)

    # write modified data back to rom
    write_file(output_file, output_dir, rom_data)

if __name__=="__main__":
    main()