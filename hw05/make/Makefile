.PHONEY : all clean test

-include ./path.mak

CC := $(LINUXarm_GCC)
CFLAGS := -g
LINKER_FLAGS := -lstdc++

all : app.arm

app.arm : app.o
	$(CC) $(CFLAGS) $(LINKER_FLAGS) $< -o $@
	@echo; echo $@ successfully created; echo

%.o : %.c
	$(CC) $(CFLAGS)  -c $< -o $@

test :
	@echo CC = $(CC)

clean:
	rm -f app.o app.arm
