.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object

.method public static foo(I)I
Label0:
.var 0 is a I from Label0 to Label1
Label2:
	iconst_1
	ireturn
Label3:
Label1:
.limit stack 2
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label2:
	iconst_1
	invokestatic MiniGoClass/foo(I)I
	invokestatic MiniGoClass/foo(I)I
	invokestatic io/putInt(I)V
	iconst_1
	invokestatic MiniGoClass/foo(I)I
	iconst_1
	invokestatic MiniGoClass/foo(I)I
	invokestatic io/putIntLn(I)V
Label3:
Label1:
	return
.limit stack 5
.limit locals 1
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
