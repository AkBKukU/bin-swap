# BIN/CUE Byte Swap

This is a simple script to allow you to swap 16 bit values between little endian and big endian. Or put another way, lets you swap byte pairs.

The purpose is for BIN/CUE files that have audio tracks. You can run into issues with different programs or tools that expect the audio to be ordered one way or the other without an option to correct it on the fly. Using this tool will allow you to correct this issue by creating a new  BIN file that has bytes swapped after a specific point.

## Usage

The function is to directly copy a binary data file up to a point. After that point the data is copied by alternating the bytes. The application of this is to skip past an ISO9660 data track in a BIN and then swap all of the audio track bytes after it. Two ways have been provided to specify the end of the data track.

### Seek
Using `-s` or `--seek` you can specify the number of 16 bit byte pairs to directly copy before starting to swap.

### Time
Using `-t` or `--time` you can use an `INDEX` value from a CUE sheet as your swap point. These values are in a Minutes/Seconds/Frames format (Note: there are 75 frames per second).

It would be convenient to be able to pass a CUE file and use the `INDEX` time from the first audio track. But CUE sheets are not well standardized and dealing with `PREGAP` and `INDEX 00` that change where the swap should happen. I've not been able to confirm how these should be handled to get the correct byte position.

## Help Output

	usage: BIN/CUE Byte swap [-h] [-t TIME] [-s SEEK] [-o OUTPUT] [bin_name]

	Allows you to byte swap only audio tracks in a BIN file. This assumes a 16 bit data type and
	swaps the two 8 bit segments.

	positional arguments:
	bin_name

	options:
	-h, --help            show this help message and exit
	-t TIME, --time TIME  CUE timestamp of first INDEX to seek to
	-s SEEK, --seek SEEK  Seek number of frames (u16) into BIN
	-o OUTPUT, --output OUTPUT
				Output filename
