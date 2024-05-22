bits 16     ; We're dealing with 16 bit code (Real Mode)
org 0x7c00  ; Inform the assembler of the starting location for this code
jmp CODE
CODE:
    xor ax, ax ; Limpa registrador ax
    mov ds, ax ; Limpa o Segmento de Dados
    mov es, ax ; Limpa o Segmento de Extra
    mov ss, ax ; Limpa o Segmento de Pilha

    call ivtm_config

    mov ax, di
    push ax                 ;passa será vai armazenar a string
    call get_keyboard_input ;pega input armazena string iniciando no endereço ax

    
    int 0x40;ax, o endereço da string, já está na pilha



    jmp $  ; halt (hlt também funciona)

ivtm_config:
    push ax
    push di
    push ds
        xor ax,ax 
        mov ds, ax                      ; apenas para garantir que ds será 0

        mov di, 0x100                   ;move para di o endereço onde vai ficar a interrupção (40h *4)
        mov word[di], print_string      ;move ip da int 40h para di
        mov word[di+2], 0               ;move cs da int 40h para di + 2
    pop ds
    pop di
    pop ax
    ret
print_string:
    push bp ; salvar o valor de bp
    mov bp, sp
    mov ax, [bp+8]
    mov si, ax
    .loop:
        ;; carrega do si um byte em ax
        lodsb
        or al, al
        jz .done
        mov ah, 0x0E
        int 0x10
        jmp .loop
    .done:
    pop bp ;; devolver o valor antigo de bp
    iret  ;; n parametros * 2 (modo real)
get_keyboard_input: ;recebe input do teclado e coloca input em di
    pusha
    push di 

    push bp             ;armazena bp na pilha
    mov bp,sp           ;move sp para bp
    add bp, 6           ;adiciona 6 bytes para pular bp, di e ip
    mov di, word[bp]    ;pega o argumento e coloca em di 
    pop bp         

    .loop:
        mov ah, 0x00    ;interrupção de input do teclado
        int 0x16        ;recebe input do teclado e armazena em al
        stosb           ;armazena caracter que foi lido em es:di
        cmp al, 0x0D    ;compara caracter recebido com enter
        je .done
    jmp .loop
    .done:

    pop di
    popa
    ret
times 510-($-$$) db 0 ; Add any additional zeroes to make 510 bytes in total
dw 0xAA55 ; Write the final 2 bytes as the magic number 0x55aa, remembering x86 little endian

