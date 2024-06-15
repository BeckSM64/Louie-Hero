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

// Remove Bomberman model from Louie's back
.org 0x00149B40
hex { 24 06 00 12 }

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

// Replace enemy at top of Aqua Tank with beam to end level
// TODO: Beam goes through the floor and can be triggered early, fix this
.org 0x002225B0
hex { 01 90 }

// Replace final turret with box in Aquaway
.org 0x00222780
hex { 00 41 03 A2 }

// Make beam work with Louie in Move Stone
.org 0x000DE690
OR A0, R0, R0
JAL 0x00069E68
ADDIU A1, R0, 0x0001

// Force beam to already have spawned on start of Move Stone
.org 0x0001A800
ORI T6, R0, 0x0004
SH T6, 0x00B2 (T7)
.org 0x0008F424
NOP
NOP

// Remove snake boss from Heaven Sky and replace with beam
.org 0x00224C30
hex { 01 90 }
.org 0x00224C40
NOP
.org 0x00224C50
NOP

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

// Add beam to bubble hole
// TODO: Fix so game doesn't crash when touching bouncy terrain
.org 0x0021E5B0
hex { 01 90 }

// Add boxes to middle of pit in hard coaster
.org 0x00222D70
hex { 00 41 01 DF 00 00 01 D7 }
.org 0x00222D60
hex { 00 41 01 DF 00 00 02 55 }
.org 0x00222D50
hex { 00 41 01 DF 00 00 01 59 }

// Force Door to be open already in Hard Coaster
.org 0x0007A584 // Address in RAM: 0x80088060
SB T4, 0x523C (AT)

.org 0x002233E0
hex { 01 90 00 5A 02 1C 0B B8}
