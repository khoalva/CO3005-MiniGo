.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label2:
	iconst_2
	anewarray [F
	dup
	iconst_0
	iconst_2
	newarray float
	dup
	iconst_0
	ldc 0.0
	fastore
	dup
	iconst_1
	ldc 0.0
	fastore
	aastore
	dup
	iconst_1
	iconst_2
	newarray float
	dup
	iconst_0
	ldc 0.0
	fastore
	dup
	iconst_1
	ldc 0.0
	fastore
	aastore
.var 1 is a [[F from Label2 to Label3
	astore_1
	aload_1
	iconst_1
	aaload
	iconst_0
	bipush 10
	i2f
	fastore
	aload_1
	iconst_1
	aaload
	iconst_0
	faload
	invokestatic io/putFloat(F)V
Label3:
Label1:
	return
.limit stack 10
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
