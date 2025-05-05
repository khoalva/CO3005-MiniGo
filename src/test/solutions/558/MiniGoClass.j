.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label2:
	new Test
	dup
	invokespecial Test/<init>()V
.var 1 is a LTest; from Label2 to Label3
	astore_1
	aload_1
	iconst_5
	putfield Test/x I
	aload_1
	bipush 10
	putfield Test/y I
	aload_1
	getfield Test/x I
	invokestatic io/putInt(I)V
Label3:
Label1:
	return
.limit stack 4
.limit locals 2
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
