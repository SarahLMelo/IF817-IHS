section .data
three dq 3.0

section .text

global calc_volume_cone

calc_volume_cone:

;; criar novo stack frame
push ebp
mov ebp, esp

;; inicia a FPU
finit

;; calula volume do cone
fldpi               ;; Pi em st0
fld dword[ebp + 8]  ; r em st0, PI em st1
fld dword[ebp + 12] ; h em st0, r em st1, PI em st2
fmul st1           ;; h * r em st0, r em st1, PI em st2
fmulp st1, st0     ;; h * r² em st0, PI em st1
fmulp st1, st0     ;; h * r² * PI em st0
fld qword[three]   ;; 3.0 em st0, h * r² * PI em st1
fdivr st1          ;; (h * r² * PI)/3.0 em st0, h * r² * PI em st1


;; destroi stack frame
mov esp, ebp
pop ebp

;; retorna. retorno em st0
ret
