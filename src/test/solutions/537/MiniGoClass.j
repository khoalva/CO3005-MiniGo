.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label2:
.var 1 is a I from Label2 to Label3
.var 1 is a I from Label2 to Label3
	iconst_0
	istore_1
Label4:
	iload_1
	iconst_5
	if_icmpge Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifle Label5
Label8:
	iload_1
	iconst_3
	if_icmpne Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	ifle Label10
Label14:
	goto Label5
Label15:
Label10:
	iload_1
	invokestatic io/putInt(I)V
	iload_1
	iconst_1
	iadd
	istore_1
Label9:
	goto Label4
Label5:
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
