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
	new Test1
	dup
	invokespecial Test1/<init>()V
.var 2 is b LTest1; from Label2 to Label3
	astore_2
	new Test2
	dup
	invokespecial Test2/<init>()V
.var 3 is c LTest2; from Label2 to Label3
	astore_3
	aload_3
	iconst_5
	putfield Test2/z I
	aload_2
	aload_3
	putfield Test1/y LTest2;
	aload_1
	aload_2
	putfield Test/x LTest1;
	aload_1
	getfield Test/x LTest1;
	getfield Test1/y LTest2;
	getfield Test2/z I
	invokestatic io/putInt(I)V
Label3:
Label1:
	return
.limit stack 3
.limit locals 4
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
