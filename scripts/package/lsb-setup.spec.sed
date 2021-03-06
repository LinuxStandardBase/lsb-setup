# %{ver}, %{rel} are provided my the Makefile
%define ver @VERSION@
%define rel @RELEASE@
%define basedir /opt/lsb
 
# %{version}, %{rel} are provided by the Makefile
Summary: LSB setup
Name: lsb-setup
Version: %{ver}
Release: %{rel}
License: GPL
Group: Development/Tools
URL: http://www.linuxfoundation.org/bzr/unofficial/lsb-setup
BuildRoot: %{_tmppath}/%{name}-root
AutoReqProv: no
BuildArch: noarch
Requires: lsb

%description
Basic LSB /opt/lsb filesystem package

#==================================================
%prep

#==================================================
%build

#==================================================
%install

rm -rf ${RPM_BUILD_ROOT}
mkdir -p ${RPM_BUILD_ROOT}%{basedir}/{bin,doc,include,share,test,man/{man1,man3}}

%pre
# since we do not own /opt. and debian/ubuntu pkgs do not either
# it's possible to lose /opt altogether with installs/uninstalls
# and then the perms are all messed up for the next cycle
if [ ! -d /opt ];then
  mkdir /opt
  chown root:root /opt
  chmod 0755 /opt
fi

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
%dir %{basedir}/include
%dir %{basedir}/share
%dir %{basedir}/test
%dir %{basedir}/man
%dir %{basedir}/man/man1
%dir %{basedir}/man/man3

#==================================================
%changelog
* Fri Nov 21 2008 Stew Benedict <stewb@linux-foundation.org>
- only require "lsb"

* Sat Nov 08 2008 Stew Benedict <stewb@linux-foundation.org>
- own /opt/lsb/include

* Wed Nov 05 2008 Stew Benedict <stewb@linux-foundation.org>
- own /opt/lsb/lib{64}
- manage the updates from beta/snapshots for the lib/lib-4.0 swap

* Fri Sep 26 2008 Stew Benedict <stewb@linux-foundation.org>
- initial package
