%define basedir /opt/lsb
 
# %{version}, %{rel} are provided by the Makefile
Summary: LSB setup
Name: lsb-setup
Version: %{version}
Release: %{rel}
License: GPL
Group: Development/Tools
URL: http://www.linuxfoundation.org/bzr/unofficial/lsb-setup
BuildRoot: %{_tmppath}/%{name}-root
AutoReqProv: no
BuildArch: noarch
Requires: lsb >= 4.0

%description
Basic LSB /opt/lsb filesystem package

#==================================================
%prep

#==================================================
%build

#==================================================
%install

rm -rf ${RPM_BUILD_ROOT}
mkdir -p ${RPM_BUILD_ROOT}%{basedir}/{bin,doc,share,man/{man1,man3}}

#==================================================
%clean
if [ -z "${RPM_BUILD_ROOT}"  -a "${RPM_BUILD_ROOT}" != "/" ]; then 
    rm -rf ${RPM_BUILD_ROOT}
fi

#==================================================
%files
%defattr(0755,root,root)
%dir %{basedir}
%dir %{basedir}/bin
%dir %{basedir}/doc
%dir %{basedir}/share
%dir %{basedir}/man
%dir %{basedir}/man/man1
%dir %{basedir}/man/man3

#==================================================
%changelog
* Fri Sep 26 2008 Stew Benedict <stewb@linux-foundation.org>
- initial package
