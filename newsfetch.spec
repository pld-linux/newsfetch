Summary: Most Compact and Powerfull newsfetching utility 
Name: newsfetch
Version: 1.11
Release: 1
Copyright: shareware
Group: Applications/News
Source: ftp://sunsite.unc.edu/pub/Linux/system/news/readers/newsfetch-1.11.tar.gz
%description
newsfetch is a powerfull utility to fetch news from an NNTP server and 
stores in the mailbox format. The files created by newsfetch can be used 
with any mail reader.
%prep
%setup

%build
make

%install
install -s -m 755 -o 0 -g 0 ./newsfetch /usr/bin/newsfetch
install -m 644 -o 0 -g 0 ./newsfetch.1 /usr/man/man1

%files
%doc README CHANGES
/usr/bin/newsfetch
/usr/man/man1/newsfetch.1
