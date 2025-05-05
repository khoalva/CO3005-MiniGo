.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label2:
.var 1 is a LTest1; from Label2 to Label3
	new Test1
	dup
	invokespecial Test1/<init>()V
	dup
	iconst_1
	putfield Test1/x I
	dup
	iconst_2
	putfield Test1/y I
	astore_1
.var 2 is c LTest; from Label2 to Label3
	new Test
	dup
	invokespecial Test/<init>()V
	dup
	aload_1
	putfield Test/x LTest1;
	astore_2
	aload_2
	new Test1
	dup
	invokespecial Test1/<init>()V
	dup
	iconst_3
	putfield Test1/x I
	dup
	iconst_4
	putfield Test1/y I
	putfield Test/x LTest1;
	aload_2
	getfield Test/x LTest1;
	getfield Test1/y I
	invokestatic io/putInt(I)V
Label3:
Label1:
	return
.limit stack 7
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
