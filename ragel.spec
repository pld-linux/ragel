Summary:	Ragel State Machine Compiler
Summary(pl.UTF-8):	Ragel State Machine Compiler - kompilator automatów
Name:		ragel
Version:	7.0.4
Release:	1
License:	MIT
Group:		Development/Tools
Source0:	http://www.colm.net/files/ragel/%{name}-%{version}.tar.gz
# Source0-md5:	2ca4f5507c1923bcf9a7909baa8254d3
URL:		http://www.colm.net/open-source/ragel/
BuildRequires:	asciidoc
BuildRequires:	colm = 0.14.7
BuildRequires:	colm-devel = 0.14.7
BuildRequires:	dblatex
BuildRequires:	rpm-build >= 4.6
BuildRequires:	libstdc++-devel
BuildRequires:	libxml2-progs
BuildRequires:	libxslt-progs
BuildRequires:	texlive-format-pdflatex
BuildRequires:	texlive-xetex
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

%package doc
Summary:	Documentation for Ragel
Summary(pl.UTF-8):	Dokumentacja do pakietu Ragel
Group:		Documentation
BuildArch:	noarch

%description doc
Documentation for Ragel.

%description doc -l pl.UTF-8
Dokumentacja do pakietu Ragel.

%package -n vim-syntax-ragel
Summary:	Vim syntax file for Ragel
Summary(pl.UTF-8):	Plik składni Vima dla pakietu Ragel
Group:		Applications/Editors
Requires:	vim-rt
BuildArch:	noarch

%description -n vim-syntax-ragel
Vim syntax file for Ragel.

%description -n vim-syntax-ragel -l pl.UTF-8
Plik składni Vima dla pakietu Ragel.

%prep
%setup -q

%build
%configure \
	CPPFLAGS="%{rpmcppflags} -I/usr/include/aapl" \
	COLM=/usr/bin/colm \
	COLM_WRAP=/usr/bin/colm-wrap \
	COLM_SHARE=/usr/share/colm \
	LIBCOLM_LA="-lcolm" \
	LIBFSM_LA="-lfsm" \
	--datadir=%{_datadir}/ragel \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# API not exported
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libragel.{so,la}

# packaged as %doc
%{__rm} $RPM_BUILD_ROOT%{_docdir}/ragel/ragel-guide.*

install -d $RPM_BUILD_ROOT%{_datadir}/vim/vimfiles/syntax
%{__mv} $RPM_BUILD_ROOT%{_docdir}/ragel/ragel.vim $RPM_BUILD_ROOT%{_datadir}/vim/vimfiles/syntax

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING README
%attr(755,root,root) %{_bindir}/ragel
%attr(755,root,root) %{_bindir}/ragel-asm
%attr(755,root,root) %{_bindir}/ragel-c
%attr(755,root,root) %{_bindir}/ragel-crack
%attr(755,root,root) %{_bindir}/ragel-csharp
%attr(755,root,root) %{_bindir}/ragel-d
%attr(755,root,root) %{_bindir}/ragel-go
%attr(755,root,root) %{_bindir}/ragel-java
%attr(755,root,root) %{_bindir}/ragel-js
%attr(755,root,root) %{_bindir}/ragel-julia
%attr(755,root,root) %{_bindir}/ragel-ocaml
%attr(755,root,root) %{_bindir}/ragel-ruby
%attr(755,root,root) %{_bindir}/ragel-rust
%attr(755,root,root) %{_libdir}/libragel.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libragel.so.0
%{_datadir}/ragel
%{_mandir}/man1/ragel.1*

%files doc
%defattr(644,root,root,755)
%doc doc/ragel/{ragel-guide.html,*.png}

%files -n vim-syntax-ragel
%defattr(644,root,root,755)
%{_datadir}/vim/vimfiles/syntax/ragel.vim
