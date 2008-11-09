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
mkdir -p ${RPM_BUILD_ROOT}%{basedir}/{bin,doc,include,share,test,man/{man1,man3}}
mkdir ${RPM_BUILD_ROOT}%{basedir}/lib
mkdir ${RPM_BUILD_ROOT}%{basedir}/lib64

#=================================================
# this whole dance is to handle upgrades from 4.0 beta/snapshots
%pre
if [ -d /opt/lsb/lib-4.0 -a -h /opt/lsb/lib ];then
  mv /opt/lsb/lib-4.0 /opt/lsb/lib-4.0.old
  rm -f /opt/lsb/lib
fi
if [ -d /opt/lsb/lib64-4.0 -a -h /opt/lsb/lib64 ];then
  mv /opt/lsb/lib64-4.0 /opt/lsb/lib64-4.0.old
  rm -f /opt/lsb/lib64
fi

%post
if [ -d /opt/lsb/lib-4.0.old ];then
  cd /opt/lsb/lib-4.0.old
  for file in `find .`;do
    if [ ! -e /opt/lsb/lib/$file ];then
      mv $file /opt/lsb/lib/$file
    fi
  done
  rm -fr /opt/lsb/lib-4.0.old
  cd /opt/lsb
  if [ ! -e lib-4.0 ];then
    ln -s lib lib-4.0
  fi
fi
if [ -d /opt/lsb/lib64-4.0.old ];then
  cd /opt/lsb/lib64-4.0.old
  for file in `find .`;do
    if [ ! -e /opt/lsb/lib64/$file ];then
      mv $file /opt/lsb/lib64/$file
    fi
  done
  rm -fr /opt/lsb/lib64-4.0.old
  cd /opt/lsb
  if [ ! -e lib64-4.0 ];then
    ln -s lib64 lib64-4.0
  fi
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
%dir %{basedir}/lib
%dir %{basedir}/lib64

#==================================================
%changelog
* Sat Nov 08 2008 Stew Benedict <stewb@linux-foundation.org>
- own /opt/lsb/include

* Wed Nov 05 2008 Stew Benedict <stewb@linux-foundation.org>
- own /opt/lsb/lib{64}
- manage the updates from beta/snapshots for the lib/lib-4.0 swap

* Fri Sep 26 2008 Stew Benedict <stewb@linux-foundation.org>
- initial package
