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

.method public NewTest(II)V
Label0:
.var 1 is x I from Label0 to Label1
.var 2 is y I from Label0 to Label1
Label2:
	aload_0
	iload_1
	putfield Test/x I
	aload_0
	iload_2
	putfield Test/y I
Label3:
Label1:
	return
.limit stack 2
.limit locals 3
.end method
