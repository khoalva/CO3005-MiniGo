.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label2:
.var 1 is a I from Label2 to Label3
	iconst_0
	istore_1
Label7:
	iload_1
	iconst_5
	if_icmpge Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	ifle Label6
Label10:
	iload_1
	invokestatic io/putInt(I)V
	iload_1
	iconst_1
	iadd
	istore_1
Label11:
	goto Label7
Label6:
Label3:
Label1:
	return
.limit stack 6
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
