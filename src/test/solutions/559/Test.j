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

.method public static foo()I
Label0:
Label2:
	getstatic Test/a <class 'AST.Id'>
	getfield Test/x I
	getstatic Test/a <class 'AST.Id'>
	getfield Test/y I
	iadd
	ireturn
Label3:
Label1:
.limit stack 2
.limit locals 0
.end method
