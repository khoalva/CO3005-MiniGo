.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label2:
	new PPL3
	dup
	invokespecial PPL3/<init>()V
	dup
	iconst_1
	putfield PPL3/number I
	new PPL3
	invokespecial PPL3/<init>()V
.var 1 is a LPPL3; from Label2 to Label3
	astore_1
	aload_1
	new Study
	invokespecial Study/<init>()V
.var 2 is b LStudy; from Label2 to Label3
	astore_2
	aload_1
	new Play
	invokespecial Play/<init>()V
.var 3 is c LPlay; from Label2 to Label3
	astore_3
Label3:
Label1:
	return
.limit stack 4
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
