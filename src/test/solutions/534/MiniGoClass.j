.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object

.method public static foo1(I)I
Label0:
.var 0 is x I from Label0 to Label1
Label2:
	iload_0
	iconst_1
	iadd
	ireturn
Label3:
Label1:
.limit stack 3
.limit locals 1
.end method

.method public static foo2(II)I
Label0:
.var 0 is x I from Label0 to Label1
.var 1 is y I from Label0 to Label1
Label2:
	iload_0
	iload_1
	iadd
	ireturn
Label3:
Label1:
.limit stack 2
.limit locals 2
.end method

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label2:
.var 1 is a I from Label2 to Label3
.var 1 is a I from Label2 to Label3
	iconst_5
	invokestatic MiniGoClass/foo1(I)I
	istore_1
.var 2 is b I from Label2 to Label3
.var 2 is b I from Label2 to Label3
	iload_1
	bipush 10
	invokestatic MiniGoClass/foo2(II)I
	istore_2
	iload_2
	invokestatic io/putInt(I)V
Label3:
Label1:
	return
.limit stack 4
.limit locals 3
.end method

.method public <init>()V
.var 0 is this LMiniGoClass; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public static <clinit>()V
Label0:
Label1:
	return
.limit stack 0
.limit locals 0
.end method
