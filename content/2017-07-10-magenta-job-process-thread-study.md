Title: Magenta Job/Process/Thread Study
Date: 2017-07-10 05:59
Modified: 2017-07-10 05:59
Category: Archive
Tags: 
Authors: Solring Lin
Summary: (archive) Magenta Job/Process/Thread Study


Magenta Job/Process/Thread Study
===================

# Thread

syscall: kernel/lib/syscalls/syscalls_task.cpp
sys_thread_create
-->  process->CreateUserThread
----> ut->Initialize(name.data(), name.length());

source: kernel/lib/magenta/user_thread.cpp

## Init. flow

1. allocate_stack
2. new a LK thread
	assign *user_thread* to itself
	register thread state change callback
3. attach process address space
	*vmm_aspace*

## Thread Stucture

header: include/kernel/thread.h
最新LK的thread: https://github.com/littlekernel/lk/blob/master/include/kernel/thread.h
^ 已經有VMM, SMP相關的欄位

AOSP Trusty裡面LK的thread: https://android.googlesource.com/trusty/lk/common/+/master/include/kernel/thread.h
^ 比較舊

## New attributes in Magenta
1. user thread related
2. signal
3. priority boost
4. interruptable
5. profiling & debug related
6. default一定有vmm_aspace
7. default一定有SMP

## Thread context switch

source: kernel/kernel/thread.c

void thread_resched(void)

---> void vmm_context_switch(vmm_aspace_t* oldspace, vmm_aspace_t* newaspace)  kernel/kernel/vm/vmm.c

-----> arch_mmu_context_switch (Platform dependent here) // change VM space


# Process

source: kernel/lib/magenta/process_dispatcher.cpp

# System Call kernel entries

source location: kernel/lib/syscalls/

接到各個kernel space object dispatcher

