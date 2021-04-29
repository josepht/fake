Name:       fake
Version:    1.1
Release:    28%{?dist}
Summary:    fake package
License:    GPL
Group:      System Environment/Base
# Epoch:      7
# Source:     foo.txt
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
%description
fake

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/bin
touch $RPM_BUILD_ROOT/usr/bin/nosuchfile

#if test "%{?dist}" != ".el7j9"; then
#    echo "WRONG DIST TAG"
#    # exit 1
#fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
/usr/bin/nosuchfile

