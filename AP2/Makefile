#para rodar o default, é necessário o boot.bin
defalt: boot.bin
	qemu-system-x86_64 -drive format=raw,file=boot.bin
#para gerar o boot.bin, é necessário o boot.asm
boot.bin: boot.asm 
	nasm -f bin boot.asm -o boot.bin
clean:
	$(RM) count *.bin *~