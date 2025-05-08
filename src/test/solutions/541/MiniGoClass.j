.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object
.field static final a I
.field static final b I

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label2:
	getstatic MiniGoClass/a I
	getstatic MiniGoClass/b I
	iadd
	invokestatic io/putInt(I)V
Label3:
Label1:
	return
.limit stack 2
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
	iconst_5
	iconst_5
	iadd
	putstatic MiniGoClass/a I
	bipush 10
	putstatic MiniGoClass/b I
Label1:
	return
.limit stack 4
.limit locals 0
.end method
