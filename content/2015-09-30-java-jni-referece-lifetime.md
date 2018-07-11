Title: [Java] JNI referece lifetime
Date: 2015-09-30 02:40
Modified: 2015-09-30 02:40
Category: Archive
Tags: 
Authors: Solring Lin
Summary: (archive) [Java] JNI referece lifetime


https://www3.ntu.edu.sg/home/ehchua/programming/java/JavaNativeInterface.html
http://docs.oracle.com/javase/7/docs/technotes/guides/jni/spec/types.html

1. A local reference is created within the native method, and freed once the method exits. It is valid for the duration of a native method. You can also use JNI function DeleteLocalRef() to invalidate a local reference explicitly, so that it is available for garbage collection intermediately. 
	所以實際上的回收還是由GC負責。先被free的reference比較可能先被回收
  
2. Objects are passed to native methods as local references. All Java objects (jobject) returned by JNI functions are local references.
	所以如果還要在別的native function裡使用這個reference要再另外建Global ref

2. A global reference remains until it is explicitly freed by the programmer, via the DeleteGlobalRef() JNI function. You can create a new global reference from a local reference via JNI function NewGlobalRef().

3. Reference type (jobject): jclass, jmethodID, jfieldID, jarray, jexception, jstring