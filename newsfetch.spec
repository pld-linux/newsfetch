Summary:	Most Compact and Powerfull newsfetching utility 
Summary(pl):	Narzêdzie do przesy³ania artyku³ów NEWS.
Name:		newsfetch
Version:	1.11
Release:	1
Copyright:	shareware
Group:		Applications/News
Source:		ftp://sunsite.unc.edu/pub/Linux/system/news/readers/%{name}-%{version}.tar.gz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Newsfetch is a powerfull utility to fetch news from an NNTP server and
stores in the mailbox format. The files created by newsfetch can be used
with any mail reader.

%description -l pl
Newsfetch jest niezwykle wydajnym narzêdziem pozwalaj±cym na przesy³anie
artyku³ów z serwera NNTP i umieszczanie ich w pliku o formacje mailboxa.
Pliki stworzone przez newsfetch mog± byæ odczytane przez dowolnego klienta
pocztowego.

%prep
%setup -q

%build
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install -s newsfetch $RPM_BUILD_ROOT%{_bindir}/newsfetch
install newsfetch.1 $RPM_BUILD_ROOT%{_mandir}/man1

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/* README CHANGES

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz CHANGES.gz
%attr(755,root,root) %{_bindir}/newsfetch
%{_mandir}/man1/newsfetch.1.gz
