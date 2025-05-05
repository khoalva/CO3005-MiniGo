.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object
.field static final a LTest;
.field static final b LTest;

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label2:
	getstatic MiniGoClass/a LTest;
	getfield Test/x I
	invokestatic io/putInt(I)V
Label3:
Label1:
	return
.limit stack 1
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
	new Test
	dup
	invokespecial Test/<init>()V
	dup
	iconst_1
	putfield Test/x I
	dup
	iconst_2
	putfield Test/y I
	putstatic MiniGoClass/a LTest;
	new Test
	dup
	invokespecial Test/<init>()V
	dup
	iconst_3
	putfield Test/x I
	dup
	iconst_4
	putfield Test/y I
	putstatic MiniGoClass/b LTest;
Label1:
	return
.limit stack 7
.limit locals 0
.end method
