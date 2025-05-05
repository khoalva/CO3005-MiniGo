.source Test.java
.class public Test
.super java.lang.Object
.field x I
.field y I

.method public <init>()V
.var 0 is this LTest; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public foo1()I
Label0:
Label2:
	iconst_5
.var 1 is x I from Label2 to Label3
	istore_1
	iload_1
	aload_0
	getfield Test/x I
	iadd
	ireturn
Label3:
Label1:
.limit stack 3
.limit locals 2
.end method

.method public foo()I
Label0:
Label2:
	aload_0
	getfield Test/x I
	aload_0
	getfield Test/y I
	iadd
	ireturn
Label3:
Label1:
.limit stack 2
.limit locals 1
.end method

.method public bar()I
Label0:
Label2:
	aload_0
	getfield Test/x I
	aload_0
	getfield Test/y I
	imul
	ireturn
Label3:
Label1:
.limit stack 2
.limit locals 1
.end method
