Summary:	Ragel State Machine Compiler
Name:		ragel
Version:	5.16
Release:	1
License:	GPL
Group:		Development/Tools
URL:		http://www.cs.queensu.ca/home/thurston/ragel/
Source0:	http://www.cs.queensu.ca/home/thurston/ragel/%{name}-%{version}.tar.gz
# Source0-md5:	0c19b9fe68dd54efa64009dc85a08325
BuildRequires:	bison
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ragel compiles finite state machines from regular languages into
runnable C code. Ragel state machines can not only recognize byte
sequences as regular expression machines do, but can also execute code
at arbitrary points in the recognition of a regular language. When you
wish to write down a regular language you start with some simple
regular language and build a bigger one using the regular language
operators union, concatenation, kleene star, intersection and
subtraction. This is precisely the way you describe to Ragel how to
compile your finite state machines. Ragel also understands operators
that insert function calls into machines and operators that control
any non-determinism in machines.

%prep
%setup -q

%build
%configure
%{__make}
cd doc
%{__make} ragel.1 rlcodegen.1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install -s ragel/ragel $RPM_BUILD_ROOT%{_bindir}/ragel
install -s rlcodegen/rlcodegen $RPM_BUILD_ROOT%{_bindir}/rlcodegen
install -d $RPM_BUILD_ROOT%{_mandir}/man1
install doc/ragel.1 $RPM_BUILD_ROOT%{_mandir}/man1/ragel.1
install doc/rlcodegen.1 $RPM_BUILD_ROOT%{_mandir}/man1/rlcodegen.1

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*

%clean
rm -rf $RPM_BUILD_ROOT
