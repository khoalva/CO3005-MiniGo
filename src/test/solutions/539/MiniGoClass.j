.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object
.field static final a Ljava/lang/String;

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label2:
	getstatic MiniGoClass/a Ljava/lang/String;
	getstatic MiniGoClass/a Ljava/lang/String;
	invokevirtual java.lang.String/concat(Ljava/lang/String;)Ljava/lang/String;
.var 1 is b Ljava/lang/String; from Label2 to Label3
	astore_1
	aload_1
	invokestatic io/putString(Ljava/lang/String;)V
Label3:
Label1:
	return
.limit stack 2
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
	ldc "votien"
	putstatic MiniGoClass/a Ljava/lang/String;
Label1:
	return
.limit stack 1
.limit locals 0
.end method
