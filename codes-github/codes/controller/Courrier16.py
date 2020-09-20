from math import ceil
Font=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x02\x00\x02\x00\x02\x00\x02\x00\x02\x00\x02\x00\x02\x00\x02\x00\x00\x00\x00\x00\x07\x00\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x009\xc09\xc09\xc0\x10\x80\x10\x80\x10\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x80\x04\x80\x04\x80\t\x00\t\x00?\xc0\t\x00\t\x00\t\x00?\xc0\t\x00\t\x00\x12\x00\x12\x00\x12\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x02\x00\x0f\xc0\x10@\x10\x00\x10\x00\x0c\x00\x03\x80\x00@\x00@\x10@\x10\xc0\x1f\x80\x02\x00\x02\x00\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1c\x00"\x00"\x00"\x00\x1c\x00\x00\xc0\x0f\x000\x00\x03\x80\x04@\x04@\x04@\x03\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\x80\x08\x00\x08\x00\x08\x00\x04\x00\x0e\x00\x12`\x11@\x11\x80\x11\x80\x0e`\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\x00\x07\x00\x07\x00\x02\x00\x02\x00\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x00\x80\x01\x00\x01\x00\x02\x00\x02\x00\x02\x00\x02\x00\x02\x00\x02\x00\x02\x00\x02\x00\x01\x00\x01\x00\x00\x80\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x08\x00\x04\x00\x04\x00\x02\x00\x02\x00\x02\x00\x02\x00\x02\x00\x02\x00\x02\x00\x02\x00\x04\x00\x04\x00\x08\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x00\x04\x00\x04\x00?\xc0\x04\x00\x06\x00\t\x00\x10\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x00\x04\x00\x04\x00\x04\x00\x04\x00\x7f\xc0\x04\x00\x04\x00\x04\x00\x04\x00\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0e\x00\x0c\x00\x0c\x00\x18\x00\x18\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00?\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0e\x00\x0e\x00\x0e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00@\x00@\x00\x80\x00\x80\x01\x00\x01\x00\x02\x00\x02\x00\x04\x00\x04\x00\x08\x00\x08\x00\x10\x00\x10\x00 \x00 \x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\x80\x18@\x10@              \x10@\x10@\x0f\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x06\x00:\x00\x02\x00\x02\x00\x02\x00\x02\x00\x02\x00\x02\x00\x02\x00\x02\x00\x02\x00\x02\x00?\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f\x00\x10\x80 @ @\x00@\x00\x80\x01\x00\x02\x00\x04\x00\x08\x00\x10\x00 @?\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f\x800@\x00 \x00 \x00@\x07\x80\x00@\x00 \x00 \x00 \x00  @\x1f\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x80\x02\x80\x04\x80\x04\x80\x08\x80\x08\x80\x10\x80 \x80?\xc0\x00\x80\x00\x80\x00\x80\x03\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1f\x80\x10\x00\x10\x00\x10\x00\x17\x00\x18\x80\x00@\x00@\x00@\x00@ @\x10\x80\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\xe0\x06\x00\x08\x00\x10\x00\x10\x00\x13\x80\x14@\x18 \x10 \x10 \x08 \x0c@\x03\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00?\xc0 @\x00@\x00\x80\x00\x80\x00\x80\x01\x00\x01\x00\x01\x00\x02\x00\x02\x00\x02\x00\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f\x00\x10\x80 @ @ @\x10\x80\x0f\x00\x10\xc0 @ @ @\x10\x80\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\x00\x08\xc0\x10@\x10 \x10 \x10 \x08`\x07\xa0\x00 \x00@\x00@\x00\x80\x1f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0e\x00\x0e\x00\x0e\x00\x00\x00\x00\x00\x00\x00\x0e\x00\x0e\x00\x0e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\x00\x07\x00\x07\x00\x00\x00\x00\x00\x00\x00\x0e\x00\x0c\x00\x18\x00\x18\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00`\x00\x80\x03\x00\x0c\x00\x10\x00`\x00\x10\x00\x0c\x00\x03\x00\x00\x80\x00`\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x7f\xf0\x00\x00\x00\x00\x7f\xf0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00`\x00\x10\x00\x0c\x00\x03\x00\x00\x80\x00`\x00\x80\x03\x00\x0c\x00\x10\x00`\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f\x80\x10@\x10 \x00 \x00 \x00\xc0\x03\x00\x02\x00\x00\x00\x00\x00\x07\x00\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f\x00\x18\x80 @ @!\xc0&@$@$@$@#\xc0 \x00 \x00\x10\x80\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00?\x00\x05\x00\x08\x80\x08\x80\x08\x80\x10@\x10@?\xe0    @\x10\xf0x\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x7f\x00\x10\x80\x10@\x10@\x10\x80\x1f\x80\x10@\x10 \x10 \x10 \x10@\x7f\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f \x10\xe0  @ @\x00@\x00@\x00@\x00@\x00  \x10@\x0f\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x7f\x80\x10@\x10 \x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10 \x10@\x7f\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x7f\xe0\x10 \x10 \x11\x00\x11\x00\x1f\x00\x11\x00\x11\x00\x10 \x10 \x10 \x7f\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x7f\xe0\x10 \x10 \x11\x00\x11\x00\x1f\x00\x11\x00\x11\x00\x10\x00\x10\x00\x10\x00\x7f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f\xa0\x10`  @\x00@\x00@\x00C\xf8@ @   \x10 \x0f\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf8\xf8        ?\xe0          \xf8\xf8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00?\xe0\x02\x00\x02\x00\x02\x00\x02\x00\x02\x00\x02\x00\x02\x00\x02\x00\x02\x00\x02\x00?\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\xf0\x00@\x00@\x00@\x00@\x00@ @ @ @ @\x10\x80\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00|\xf0\x10@\x10\x80\x11\x00\x12\x00\x14\x00\x1b\x00\x10\x80\x10@\x10@\x10 |8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00>\x00\x08\x00\x08\x00\x08\x00\x08\x00\x08\x00\x08\x00\x08\x10\x08\x10\x08\x10\x08\x10?\xf0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf0x0`(\xa0(\xa0% % " "       \xf8\xf8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf0\xf80 ( ( $ " " ! !  \xa0 `\xf8`\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f\x80\x10@  @\x10@\x10@\x10@\x10@\x10@\x10  \x10@\x0f\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00?\xc0\x08 \x08\x10\x08\x10\x08\x10\x08 \x0f\xc0\x08\x00\x08\x00\x08\x00\x08\x00?\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f\x80\x10@  @\x10@\x10@\x10@\x10@\x10@\x10  \x10@\x0f\x80\x04\x00\x0f\x10\x18\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x7f\x00\x10\x80\x10@\x10@\x10@\x10\x80\x1f\x00\x10\x80\x10@\x10@\x10 |8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f\xa0\x10`    \x10\x00\x0f\x80\x00@\x00     0@/\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00?\xe0" " " " \x02\x00\x02\x00\x02\x00\x02\x00\x02\x00\x02\x00\x0f\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf8\xf8                  \x10@\x0f\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf0\xf0@  @ @ @\x10\x80\x10\x80\t\x00\t\x00\t\x00\x06\x00\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf0x@\x10@\x10B\x10B % % % (\xa0(\xa0(\xa0\x10@\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00x\xf0\x10@\x08\x80\x08\x80\x05\x00\x02\x00\x05\x00\x08\x80\x08@\x10@  x\xf0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00x\xf0  \x10@\x08\x80\x05\x00\x05\x00\x02\x00\x02\x00\x02\x00\x02\x00\x02\x00\x0f\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00?\xe0   @ \x80\x01\x00\x02\x00\x02\x00\x04 \x08 \x10   ?\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\xc0\x02\x00\x02\x00\x02\x00\x02\x00\x02\x00\x02\x00\x02\x00\x02\x00\x02\x00\x02\x00\x02\x00\x02\x00\x02\x00\x02\x00\x03\xc0\x00\x00\x00\x00\x00\x00 \x00 \x00\x10\x00\x10\x00\x08\x00\x08\x00\x04\x00\x04\x00\x04\x00\x02\x00\x02\x00\x01\x00\x01\x00\x00\x80\x00\x80\x00@\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1e\x00\x02\x00\x02\x00\x02\x00\x02\x00\x02\x00\x02\x00\x02\x00\x02\x00\x02\x00\x02\x00\x02\x00\x02\x00\x02\x00\x02\x00\x1e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x06\x00\t\x00\t\x00\x10\x80 @\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\xf8\x04\x00\x03\x00\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f\x800@\x00@\x1f\xc0 @@@@@A\xc0>p\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xe0\x00 \x00 \x00 \x00\'\x80(`0  \x10 \x10 \x100 (@\xe7\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f\xa0\x10`   \x00 \x00 \x00  \x10@\x0f\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xe0\x00 \x00 \x00 \x0f 0\xa0@`@ @ @  `0\xe0\x0f8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f\x80\x10@    ?\xe0 \x00 \x00\x10 \x0f\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\xf0\x04\x00\x04\x00\x04\x00?\xe0\x04\x00\x04\x00\x04\x00\x04\x00\x04\x00\x04\x00\x04\x00\x1f\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f8\x10\xe0 `       `\x10\xe0\x0f \x00 \x00 \x00@\x0f\x80\x00\x00\x00\x00\x00\x00p\x00\x10\x00\x10\x00\x10\x00\x17\x80\x18@\x10 \x10 \x10 \x10 \x10 \x10 |\xf8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x02\x00\x00\x00\x00\x00\x1e\x00\x02\x00\x02\x00\x02\x00\x02\x00\x02\x00\x02\x00\x02\x00?\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x02\x00\x00\x00\x00\x00?\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x01\x80>\x00\x00\x00\x00\x00\x00\x008\x00\x08\x00\x08\x00\x08\x00\t\xe0\x08\x80\t\x00\n\x00\x0e\x00\t\x00\x08\x80\x08@8\xf0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1e\x00\x02\x00\x02\x00\x02\x00\x02\x00\x02\x00\x02\x00\x02\x00\x02\x00\x02\x00\x02\x00\x02\x00?\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xec\xc03 " " " " " " \xfb\xb8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00s\x80\x1c@\x10 \x10 \x10 \x10 \x10 \x10 |\xf8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f\x80\x10@          \x10@\x0f\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xe7\x80(@0  \x10 \x10 \x100 (@\'\x80 \x00 \x00 \x00\xf8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f8\x10\xa0 `        \x10\xe0\x0f \x00 \x00 \x00 \x00\xf8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x009\xc0\n \x0c\x00\x08\x00\x08\x00\x08\x00\x08\x00\x08\x00?\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1f\xa0 `  \x1f\x80\x00@\x00   0@/\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x08\x00\x08\x00?\xc0\x08\x00\x08\x00\x08\x00\x08\x00\x08\x00\x08\x00\x08`\x07\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00p\xe0\x10 \x10 \x10 \x10 \x10 \x10 \x10`\x0f\xb8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf8\xf0 @\x10\x80\x10\x80\x11\x00\t\x00\t\x00\x06\x00\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf8\xf8  " " \x15@\x15@\x15@\x15@\x08\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00x\xf0\x10@\x08\x80\x05\x00\x02\x00\x05\x00\x08\x80\x10@x\xf0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf0x  \x10@\x10@\x08\x80\x08\x80\x05\x00\x05\x00\x02\x00\x02\x00\x04\x00\x04\x00~\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00?\xc0 \x80!\x00\x02\x00\x04\x00\x08\x00\x10@ @?\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x80\x02\x00\x02\x00\x02\x00\x02\x00\x02\x00\x02\x00\x0c\x00\x02\x00\x02\x00\x02\x00\x02\x00\x02\x00\x02\x00\x01\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x02\x00\x02\x00\x02\x00\x02\x00\x02\x00\x02\x00\x02\x00\x02\x00\x02\x00\x02\x00\x02\x00\x02\x00\x02\x00\x02\x00\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x02\x00\x02\x00\x02\x00\x02\x00\x02\x00\x02\x00\x01\x80\x02\x00\x02\x00\x02\x00\x02\x00\x02\x00\x02\x00\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1c\x00\x16 #@\x01\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'

width=13
height=20
char_offset=ceil(width/8)*height



FontInfo =(
	3, #   Character height
	' ', #   Start character
	'~', #   End character
	
)

Font_mv=memoryview(Font)
def getChar(char):
  start=(ord(char)-32)*char_offset
  return Font_mv[start:start+char_offset]
