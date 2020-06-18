;---------------------------------------------------------
; Transcreva o pseudocódigo a seguir para assembly do Z01.1:
;
; 
;    if ( RAM[1] == 1 && RAM[2] > 2 ):
;        RAM[5] = 1
;    else
;        RAM5[6] = -2
;
;---------------------------------------------------------

leaw $1, %A      ; RAM[1] == 1
movw (%A), %D
subw %A, %D, %D
leaw $ELSE, %A
jne
nop

leaw $2, %A     ; RAM[2] > 2
movw (%A), %D
subw %D, %A, %D
leaw $ELSE, %A
jle
nop

IF:
  leaw $5, %A
  movw $1, (%A)
  leaw $END, %A
  jmp
  nop

ELSE:
  leaw $2, %A
  movw %A, %D
  negw %D
  leaw $6, %A
  movw %D, (%A)

END:
