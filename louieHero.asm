// Bake in Debug Mode
.org 0x0000262C
SB T6, 0xE41B(AT)

// NOP the instructions that prevent the game from loading with a bad CRC
.org 0x0000066C
NOP
NOP

// Force every level to use Louie as the bomber type
.org 0x000745C0
ADDIU T0, R0, $0006

// Removes interaction between Louie and launcher in Battle Room
.org 0x00078C40
ADDIU T9, R0, $0001

// Removes interaction between Louie and vents in Air Room
.org 0x00078E14
ADDIU T0, R0, $0001

// Remove the door in hades crater
.org 0x00220860
NOP
NOP

// Remove the door on the cage in death temple
.org 0x00221A30
NOP
NOP

// Replace final turret with box in Aquaway
.org 0x00222780
hex { 00 41 03 A2 }

// Remove mirror room mirror bomber
.org 0x002256E0
NOP
NOP

// Remove mirror room mirror door
.org 0x002256F0
NOP
NOP

// Remove mirror room switch
.org 0x00225700
NOP
NOP

// Remove mirror room door
.org 0x00225710
NOP
NOP

// Remove mirror room switch
.org 0x00225720
NOP
NOP

// Remove mirror room door
.org 0x00225730
NOP
NOP

// Change starting position for Rockn' Road
.org 0x000F8E24
hex { FD 6C FF E2 30 0C 00 00 }

// Change starting position for Warp Room
.org 0x000F8E3C
hex { 0A 14 00 3C 01 A4 00 00 }
