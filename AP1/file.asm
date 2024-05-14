ORG 0x7C00
BITS 16
    jmp start

string db "Hello, World! This is a test string. It has 12 vowels.", 0x0D, 0x0A, 0
msg_before db "Number of vowels: ", 0

start:
    ; inicializando registradores como zero
    xor ax, ax
    mov ds, ax
    mov es, ax
    mov ss, ax
    xor cx, cx

    lea si, [string]
    call print_string

    lea si, [msg_before]
    call print_string

    ; declarando a string a analizada
    lea si, [string]
    ; chamando a função que conta as vogais
    call conta_vogal

    ; printando o número de vogais
    mov ax, cx

    call print_number

conta_vogal:
.loop:
    lodsb

    cmp al, 0
    je .end

    cmp al, 'a'
    je .adiciona_vogal

    cmp al, 'A'
    je .adiciona_vogal

    cmp al, 'e'
    je .adiciona_vogal

    cmp al, 'E'
    je .adiciona_vogal

    cmp al, 'i'
    je .adiciona_vogal

    cmp al, 'I'
    je .adiciona_vogal

    cmp al, 'o'
    je .adiciona_vogal

    cmp al, 'O'
    je .adiciona_vogal

    cmp al, 'u'
    je .adiciona_vogal

    cmp al, 'U'
    je .adiciona_vogal

    jmp .loop

.adiciona_vogal:
    inc cx
    jmp .loop

.end:
    ret

print_string:
.loop:
    lodsb ;carrega uma letra que tiver em si para al
    or al, al ;se al for zero
    jz .done  ;pule para .done
    mov ah, 0x0E ;nesse caso, transforme ah em 14 (isso é para printar)
    int 0x10 ;printa =D
    jmp .loop ;volta para a cabeça do loop
.done:
    ret

print_number:
    mov bx, 10
    mov cx, 0
.loop1:
    mov dx, 0
    div bx
    ; resposta vai ta no ax, resto no dx
    add dx, 48
    push dx
    inc cx
    cmp ax, 0
    jne .loop1
.loop2:
    pop ax
    mov ah, 0x0E
    int 0x10
    loop .loop2
.done:
    ret

; assinatura de boot
times 510-($-$$) db 0
dw 0xAA55
