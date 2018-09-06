Name:       fake
Version:    1.1
Release:    26
Summary:    fake package
License:    GPL
Group:      System Environment/Base
# Epoch:      7
# Source:     foo.txt
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:  noarch
# trying to trigger BREW-2554
BuildRequires: asciidoc
BuildRequires: audit-libs-devel
BuildRequires: bc
BuildRequires: binutils-devel
BuildRequires: bison
BuildRequires: elfutils-devel
BuildRequires: flex
BuildRequires: gettext
BuildRequires: git
BuildRequires: hostname
BuildRequires: kmod
BuildRequires: libkcapi-hmaccalc
BuildRequires: m4
BuildRequires: ncurses-devel
BuildRequires: net-tools
BuildRequires: newt-devel
BuildRequires: numactl-devel
BuildRequires: openssl
BuildRequires: openssl-devel
BuildRequires: pciutils-devel
BuildRequires: perl-Carp
BuildRequires: perl-ExtUtils-Embed
BuildRequires: perl-devel
BuildRequires: perl-generators
BuildRequires: perl-interpreter
BuildRequires: python3-devel
BuildRequires: python3-docutils
BuildRequires: xmlto
BuildRequires: xz-devel
BuildRequires: zlib-devel

%description
fake

%build
# is /dev/null there? Can we write to it?
ls -l /dev/null
echo "Hello" >/dev/null
# can we read from it?
cat /dev/null


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/bin
touch $RPM_BUILD_ROOT/usr/bin/nosuchfile

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
/usr/bin/nosuchfile

