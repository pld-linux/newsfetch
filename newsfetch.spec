Summary:	Most Compact and Powerfull newsfetching utility
Summary(pl):	Narzêdzie do przesy³ania artyku³ów NEWS
Name:		newsfetch
Version:	1.21
Release:	3
License:	Distributable
Group:		Applications/News
Source0:	ftp://sunsite.unc.edu/pub/Linux/system/news/readers/%{name}-%{version}.tar.gz
# Source0-md5:	e343a34d50d0c304f939938a8ee6cbaf
Patch0:		%{name}-gcc3.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Newsfetch is a powerfull utility to fetch news from an NNTP server and
stores in the mailbox format. The files created by newsfetch can be
used with any mail reader.

%description -l pl
Newsfetch jest niezwykle wydajnym narzêdziem pozwalaj±cym na
przesy³anie artyku³ów z serwera NNTP i umieszczanie ich w pliku o
formacje mailboxa. Pliki stworzone przez newsfetch mog± byæ odczytane
przez dowolnego klienta pocztowego.

%prep
%setup -q
%patch0 -p1

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install newsfetch $RPM_BUILD_ROOT%{_bindir}/newsfetch
install newsfetch.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README CHANGES
%attr(755,root,root) %{_bindir}/newsfetch
%{_mandir}/man1/newsfetch.1*
