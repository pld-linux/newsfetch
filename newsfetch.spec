Summary:	Most Compact and Powerfull newsfetching utility 
Name:		newsfetch
Version:	1.11
Release:	1
Copyright:	shareware
Group:		Applications/News
Source:		ftp://sunsite.unc.edu/pub/Linux/system/news/readers/newsfetch-1.11.tar.gz
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Newsfetch is a powerfull utility to fetch news from an NNTP server and
stores in the mailbox format. The files created by newsfetch can be used
with any mail reader.

%prep
%setup -q

%build
make

%install
rm -rf $RPM_BUILD_ROOT
install -s newsfetch /usr/bin/newsfetch
install newsfetch.1 /usr/man/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc README CHANGES
/usr/bin/newsfetch
/usr/man/man1/newsfetch.1
