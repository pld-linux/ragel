Summary:	Ragel State Machine Compiler
Summary(pl.UTF-8):	Ragel State Machine Compiler - kompilator automatów
Name:		ragel
Version:	6.3
Release:	1
License:	GPL
Group:		Development/Tools
Source0:	http://www.cs.queensu.ca/home/thurston/ragel/%{name}-%{version}.tar.gz
# Source0-md5:	61b53fb53c28b31bec28da8e7bd21351
URL:		http://www.cs.queensu.ca/home/thurston/ragel/
BuildRequires:	bison
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ragel compiles finite state machines from regular languages into
runnable C code. Ragel state machines can not only recognize byte
sequences as regular expression machines do, but can also execute code
at arbitrary points in the recognition of a regular language. When you
wish to write down a regular language you start with some simple
regular language and build a bigger one using the regular language
operators union, concatenation, Kleene star, intersection and
subtraction. This is precisely the way you describe to Ragel how to
compile your finite state machines. Ragel also understands operators
that insert function calls into machines and operators that control
any non-determinism in machines.

%description -l pl.UTF-8
Ragel kompiluje automaty skończone z języków regularnych do
działającego kodu w C. Automaty Ragela nie tylko rozpoznają sekwencje
bajtów, jak robią to automaty wyrażeń regularnych, ale także wykonują
kod w dowolnych miejscach podczas rozpoznawania języka regularnego.
Aby napisać język regularny zaczyna się od prostego języka regularnego
i buduje większy przy użyciu operatorów sumy, złączenia, dopełnienia
Kleene'a, przecięcia i odejmowania. Jest to dokładnie taki sposób, w
jaki opisuje się Ragelowi jak kompilować automaty skończone. Ragel
rozumie także operatory wstawiające wywołania funkcji do automatów i
operatory sterujące niedeterminizmem w automatach.

%prep
%setup -q

%build
%configure
%{__make} \
	CFLAGS="%{rpmcflags}"
%{__make} -C doc ragel.1 rlgen-cd.1 rlgen-java.1 rlgen-ruby.1 rlgen-dot.1

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	prefix=$RPM_BUILD_ROOT/usr
install -d $RPM_BUILD_ROOT%{_mandir}/man1
install doc/r*.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CREDITS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
