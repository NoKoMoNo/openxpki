#
#   - TermReadKey -
#   This spec file was automatically generated by cpan2rpm [ver: 2.027]
#   The following arguments were used:
#       --spec-only --version=2.30 '--author=Jonathan Stowe' TermReadKey-2.30.tar.gz
#   For more information on cpan2rpm please visit: http://perl.arix.com/
#

%define pkgname TermReadKey
%define filelist %{pkgname}-%{version}-filelist
%define NVR %{pkgname}-%{version}-%{release}
%define maketest 1

name:      perl-TermReadKey
summary:   TermReadKey - A perl module for simple terminal control
version:   2.30
release:   1
vendor:    Jonathan Stowe
packager:  Arix International <cpan2rpm@arix.com>
license:   Artistic
group:     Applications/CPAN
url:       http://www.cpan.org
buildroot: %{_tmppath}/%{name}-%{version}-%(id -u -n)
prefix:    %(echo %{_prefix})
source:    TermReadKey-2.30.tar.gz

%description
Term::ReadKey is a compiled perl module dedicated to providing simple
control over terminal driver modes (cbreak, raw, cooked, etc.,) support for
non-blocking reads, if the architecture allows, and some generalized handy
functions for working with terminals. One of the main goals is to have the
functions as portable as possible, so you can just plug in "use
Term::ReadKey" on any architecture and have a good likelyhood of it working.

=over 8

=item ReadMode MODE [, Filehandle]

Takes an integer argument, which can currently be one of the following 
values:

    0    Restore original settings.
    1    Change to cooked mode.
    2	 Change to cooked mode with echo off. 
          (Good for passwords)
    3    Change to cbreak mode.
    4    Change to raw mode.
    5    Change to ultra-raw mode. 
          (LF to CR/LF translation turned off) 
          
    Or, you may use the synonyms:
    
    restore
    normal
    noecho
    cbreak
    raw
    ultra-raw

These functions are automatically applied to the STDIN handle if no
other handle is supplied. Modes 0 and 5 have some special properties
worth mentioning: not only will mode 0 restore original settings, but it
cause the next ReadMode call to save a new set of default settings. Mode
5 is similar to mode 4, except no CR/LF translation is performed, and if
possible, parity will be disabled (only if not being used by the terminal,
however. It is no different from mode 4 under Windows.)

If you are executing another program that may be changing the terminal mode,
you will either want to say

    ReadMode 1
    system('someprogram');
    ReadMode 1;
    
which resets the settings after the program has run, or:

    $somemode=1;
    ReadMode 0;
    system('someprogram');
    ReadMode 1;
    
which records any changes the program may have made, before resetting the
mode.

=item ReadKey MODE [, Filehandle]

Takes an integer argument, which can currently be one of the following 
values:

    0    Perform a normal read using getc
    -1   Perform a non-blocked read
    >0	 Perform a timed read

(If the filehandle is not supplied, it will default to STDIN.) If there is
nothing waiting in the buffer during a non-blocked read, then undef will be
returned. Note that if the OS does not provide any known mechanism for
non-blocking reads, then a "ReadKey -1" can die with a fatal error. This
will hopefully not be common.

If MODE is greater then zero, then ReadKey will use it as a timeout value in
seconds (fractional seconds are allowed), and won't return "undef" until
that time expires. (Note, again, that some OS's may not support this timeout
behaviour.) If MODE is less then zero, then this is treated as a timeout
of zero, and thus will return immediately if no character is waiting. A MODE
of zero, however, will act like a normal getc.

There are currently some limitations with this call under Windows. It may be
possible that non-blocking reads will fail when reading repeating keys from
more then one console.

=item ReadLine MODE [, Filehandle]

Takes an integer argument, which can currently be one of the following 
values:

    0    Perform a normal read using scalar(<FileHandle>)
    -1   Perform a non-blocked read
    >0	 Perform a timed read

If there is nothing waiting in the buffer during a non-blocked read, then
undef will be returned. Note that if the OS does not provide any known
mechanism for non-blocking reads, then a "ReadLine 1" can die with a fatal
error. This will hopefully not be common. Note that a non-blocking test is
only performed for the first character in the line, not the entire line.
This call will probably not do what you assume, especially with
ReadMode's higher then 1. For example, pressing Space and then Backspace
would appear to leave you where you started, but any timeouts would now
be suspended.

This call is currently not available under Windows.

=item GetTerminalSize [Filehandle]

Returns either an empty array if this operation is unsupported, or a four
element array containing: the width of the terminal in characters, the
height of the terminal in character, the width in pixels, and the height in
pixels. (The pixel size will only be valid in some environments.)

Under Windows, this function must be called with an "output" filehandle,
such as STDOUT, or a handle opened to CONOUT$.

=item SetTerminalSize WIDTH,HEIGHT,XPIX,YPIX [, Filehandle]

Return -1 on failure, 0 otherwise. Note that this terminal size is only for
informative value, and changing the size via this mechanism will not
change the size of the screen. For example, XTerm uses a call like this when
it resizes the screen. If any of the new measurements vary from the old, the
OS will probably send a SIGWINCH signal to anything reading that tty or pty.

This call does not work under Windows.

=item GetSpeeds [, Filehandle]

Returns either an empty array if the operation is unsupported, or a two
value array containing the terminal in and out speeds, in decimal. E.g,
an in speed of 9600 baud and an out speed of 4800 baud would be returned as
(9600,4800). Note that currently the in and out speeds will always be
identical in some OS's. No speeds are reported under Windows.

=item GetControlChars [, Filehandle]

Returns an array containing key/value pairs suitable for a hash. The pairs
consist of a key, the name of the control character/signal, and the value
of that character, as a single character. This call does nothing under Windows.

Each key will be an entry from the following list:

	DISCARD
	DSUSPEND
	EOF
	EOL
	EOL2
	ERASE
	ERASEWORD
	INTERRUPT
	KILL
	MIN
	QUIT
	QUOTENEXT
	REPRINT
	START
	STATUS
	STOP
	SUSPEND
	SWITCH
	TIME

Thus, the following will always return the current interrupt character,
regardless of platform.

	%keys = GetControlChars;
	$int = $keys{INTERRUPT};

=item SetControlChars [, Filehandle]

Takes an array containing key/value pairs, as a hash will produce. The pairs
should consist of a key that is the name of a legal control
character/signal, and the value should be either a single character, or a
number in the range 0-255. SetControlChars will die with a runtime error if
an invalid character name is passed or there is an error changing the
settings. The list of valid names is easily available via

	%cchars = GetControlChars();
	@cnames = keys %cchars;

This call does nothing under Windows.

=back

#
# This package was generated automatically with the cpan2rpm
# utility.  To get this software or for more information
# please visit: http://perl.arix.com/
#

%prep
%setup -q -n %{pkgname}-%{version} 
chmod -R u+w %{_builddir}/%{pkgname}-%{version}

%build
grep -rsl '^#!.*perl' . |
grep -v '.bak$' |xargs --no-run-if-empty \
%__perl -MExtUtils::MakeMaker -e 'MY->fixin(@ARGV)'
CFLAGS="$RPM_OPT_FLAGS"
%{__perl} Makefile.PL `%{__perl} -MExtUtils::MakeMaker -e ' print qq|PREFIX=%{buildroot}%{_prefix}| if \$ExtUtils::MakeMaker::VERSION =~ /5\.9[1-6]|6\.0[0-5]/ '`
%{__make} 
%if %maketest
%{__make} test
%endif

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%{makeinstall} `%{__perl} -MExtUtils::MakeMaker -e ' print \$ExtUtils::MakeMaker::VERSION <= 6.05 ? qq|PREFIX=%{buildroot}%{_prefix}| : qq|DESTDIR=%{buildroot}| '`

cmd=/usr/share/spec-helper/compress_files
[ -x $cmd ] || cmd=/usr/lib/rpm/brp-compress
[ -x $cmd ] && $cmd

# SuSE Linux
if [ -e /etc/SuSE-release -o -e /etc/UnitedLinux-release ]
then
    %{__mkdir_p} %{buildroot}/var/adm/perl-modules
    %{__cat} `find %{buildroot} -name "perllocal.pod"`  \
        | %{__sed} -e s+%{buildroot}++g                 \
        > %{buildroot}/var/adm/perl-modules/%{name}
fi

# remove special files
find %{buildroot} -name "perllocal.pod" \
    -o -name ".packlist"                \
    -o -name "*.bs"                     \
    |xargs -i rm -f {}

# no empty directories
find %{buildroot}%{_prefix}             \
    -type d -depth                      \
    -exec rmdir {} \; 2>/dev/null

%{__perl} -MFile::Find -le '
    find({ wanted => \&wanted, no_chdir => 1}, "%{buildroot}");
    print "%doc  README";
    for my $x (sort @dirs, @files) {
        push @ret, $x unless indirs($x);
        }
    print join "\n", sort @ret;

    sub wanted {
        return if /auto$/;

        local $_ = $File::Find::name;
        my $f = $_; s|^\Q%{buildroot}\E||;
        return unless length;
        return $files[@files] = $_ if -f $f;

        $d = $_;
        /\Q$d\E/ && return for reverse sort @INC;
        $d =~ /\Q$_\E/ && return
            for qw|/etc %_prefix/man %_prefix/bin %_prefix/share|;

        $dirs[@dirs] = $_;
        }

    sub indirs {
        my $x = shift;
        $x =~ /^\Q$_\E\// && $x ne $_ && return 1 for @dirs;
        }
    ' > %filelist

[ -z %filelist ] && {
    echo "ERROR: empty %files listing"
    exit -1
    }

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files -f %filelist
%defattr(-,root,root)

%changelog
* Tue Dec 19 2006 root@dca02
- Initial build.