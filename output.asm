.text
.globl main
main:
li $t0, 0
move $s0, $t0
sw $s0, a

li $t1, 1
move $s0, $t1
sw $s0, z

li $t2, 2
move $s0, $t2
sw $s0, c

li $t3, 3
move $s0, $t3
sw $s0, d

li $t4, 4
move $s0, $t4
sw $s0, e

li $t5, 5
move $s0, $t5
sw $s0, f

li $t6, 6
move $s0, $t6
sw $s0, g

li $t7, 7
move $s0, $t7
sw $s0, h

li $t8, 8
move $s0, $t8
sw $s0, i

li $t9, 9
move $s0, $t9
sw $s0, p

li $t0, 10
move $s0, $t0
sw $s0, k

lw $t1, a
li $v0, 1
move $a0, $t1
syscall

lw $t2, d
li $v0, 1
move $a0, $t2
syscall

lw $t3, p
li $v0, 1
move $a0, $t3
syscall

li $v0, 10  # Exit system call
syscall

#----------------data section-------------------
.data
a: .word 0
z: .word 0
c: .word 0
d: .word 0
e: .word 0
f: .word 0
g: .word 0
h: .word 0
i: .word 0
p: .word 0
k: .word 0

