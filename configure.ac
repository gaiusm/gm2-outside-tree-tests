dnl Process this file with autoconf to produce a configure script.

AC_INIT([gm2-outside-tree-tests], [0.1], [gaiusmod2@gmail.com])
AM_INIT_AUTOMAKE([-Wno-portability])
AC_CONFIG_SRCDIR([version.c])

AC_PROG_AWK
AC_PROG_MAKE_SET

AC_PATH_PROG(GM2, gm2, /usr/bin/gm2, $PATH:/usr/bin)

AC_ARG_WITH([privatedir],
    [AS_HELP_STRING([--with-privatedir=<path>],
        [The top-level directory to the privatedir installation.])],
    [AS_IF([test -d "$with_privatedir"],
        [AC_MSG_NOTICE([Using privatedir from "$with_privatedir"])],
        [AC_MSG_ERROR([Specify an existing directory for privatedir, not "$with_privatedir"])])],
    [with_privatedir=NONE])

PRIVATEDIR_VALUE="$with_privatedir"
AC_SUBST([PRIVATEDIR_VALUE])

AC_CONFIG_FILES([
 Makefile
 runme
])

AC_OUTPUT
